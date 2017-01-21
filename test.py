import handler, random, requests, json

def function(useless_json):
    def getPrompt():
        randompost = random.randint(1,20)
        url = requests.get('https://www.reddit.com/r/WritingPrompts/hot.json', headers = {'User-agent': 'Showerthoughtbot 0.1'})
        reddit = json.loads(url.text)
        phrase= reddit['data']['children'][randompost]['data']['title']
        def remove_tags(phrase):            #removes the [??] in the beginning of the title
            phrase = phrase[4:]
            if phrase[0] == ' ':            #removes space if it exists
                phrase = phrase[1:]
            return phrase

        while phrase[0]=="[":               #handles when multiple tags exist
            phrase = remove_tags(phrase)

        return phrase
    return getPrompt()
    
if __name__ == '__main__':
    handler.invoking(function)
