import requests, feedparser, re
from googletrans import Translator

BOT_TOKEN = ''
CHANNEL_ID = ''

FEED_URL = 'https://www.upwork.com/ab/feed/jobs/rss?q=scraping&job_type=fixed&client_hires=1-9%2C10-&proposals=0-4%2C5-9%2C10-14%2C15-19&verified_payment_only=1&sort=recency&paging=0%3B10&api_params=1&securityToken=e4277010fd6bce4f39bcbe4da1a80d37ed51b03c5598f4af614d41c0c965d9b88edceeccafdb4c984998a3322293b30efccfeca7e910b593b2bc95f351eac779&userUid=1610543102364012544&orgUid=1610543102364012545'
JOBS_SENDED_TXT = 'jobs_sent.txt'

def prepare_description(description):
    cleantext = description.replace('<br />', '\n')
    cleantext = re.sub(r'\n{1,}', '\n', cleantext)
    return cleantext.replace('  ', ' ')

def jobs_sended_add_line(line):
    with open(JOBS_SENDED_TXT, "a") as file:
        file.write(line + '\n')
    jobs_sended_txt_count = sum(1 for line in open(JOBS_SENDED_TXT, 'r'))
    if jobs_sended_txt_count > 30:
        with open(JOBS_SENDED_TXT, 'r') as f:
            lines = f.readlines()
        with open(JOBS_SENDED_TXT, 'w') as f:
            f.writelines(lines[1:])

def send_message(message):
    requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(BOT_TOKEN, 'sendMessage'),
        data={
            'chat_id': CHANNEL_ID,
            'parse_mode': 'HTML',
            'text': message}
    )

def main():  
    jobs_sended = []
    with open(JOBS_SENDED_TXT, "r") as file:
        for line in file:
            jobs_sended.append(line.strip())
    rss_feed = feedparser.parse(FEED_URL)
    for entry in rss_feed.entries:
        if not entry.guid in jobs_sended:
            jobs_sended_add_line(str(entry.guid))
            message = prepare_description(entry.description)
            description = re.findall(r'(.+)(?=<b>Budget)', message.replace('\n', '**********'))
            description_array = description[0].split('**********')
            translation = []
            translator = Translator()
            for description_array_item in description_array:
                translation.append(translator.translate(description_array_item, dest="ru").text)
            translation_result = ''
            for translation_item in translation:
                translation_result += translation_item + '\n'
            message = '<b>Translation:</b>\n' + str(translation_result) + '<b>Original:</b>\n' + str(message)
            print('Notification sent successfully: ' + str(entry.link))
            send_message(message)

if __name__ == '__main__':
    main()