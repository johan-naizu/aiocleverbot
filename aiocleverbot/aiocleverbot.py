import hashlib
import re
import aiohttp

cookies = None
sessions = {}


async def cleverbot(stimulus, context=None,session=None):
    if not context:
        context=[]
    global cookies, sessions
    if (cookies is None):
        url="https://www.cleverbot.com/"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as req:
                cookies = {
                'XVIS': re.search(
                r"\w+(?=;)",
                req.headers["Set-cookie"]).group()}

    payload = f"stimulus={'%20'.join(stimulus.split())}&"

    _context = context[:]
    reverseContext = list(reversed(_context))

    for i in range(len(_context)):
        payload += f"vText{i + 2}={'%20'.join(reverseContext[i].split())}&"

    if session:
        # Creates new session if not exist
        if session not in sessions.keys():
            sessions[session] = list()

        _session = list(reversed(sessions[session]))
        # Adding the session to the payload
        for i in range(len(sessions[session])):
            payload += f"vText{i + len(_context) + 2}={'%20'.join(_session[i].split())}&"

        # Adds the context to the session
        sessions[session] = _context + sessions[session]

    payload += "cb_settings_scripting=no&islearning=1&icognoid=wsf&icognocheck="

    payload += hashlib.md5(payload[7:33].encode()).hexdigest()
    async with aiohttp.ClientSession() as session:
        async with session.post("https://www.cleverbot.com/webservicemin?uc=UseOfficialCleverbotAPI",cookies=cookies,data=payload) as req:
            getresponse = re.split(r'\\r', str(req.content))[0]
    response = getresponse[2:-1]
    if session:
        sessions[session].extend([stimulus, response])
    return response


if __name__ == "__main__":
    # With context and session
    # An ongoing conversation with the first question as "How are you?"
    print("How are you?")
    print(cleverbot(input(">>"), ["hi.", "How are you?"], "How are you?"))
    while True:
        print(cleverbot(input(">>"), session="How are you?"))
