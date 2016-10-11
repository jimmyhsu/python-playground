# API Services: Class 4 - 10/03/2016
# Google Translate API Challenge
#
# 1. Create a Python wrapper function for Translate:
#   print translate(text) -> translated_text
#
# 2. Extend your wrapper functon with target language:
#   print translate(text, language='XX') -> text in XX language
#
# 3. Extend your wrapper function to translate multiple strings:
#   print translate([text1, text2, ...], language='XX')
#   -> [text1 in XX language, text2 in XX language, ...]
#
# 4. Add Twilio SMS functionality to text the translation to you!

import httplib2
import urllib2
import json
from twilio.rest import TwilioRestClient

GOOGLE_API_KEY = "----------------------------------------------"

# Twilio Credentials
# Friendly Name: MakeSchool
TWILIO_ACCOUNT_SID = "----------------------------------------------"
TWILIO_AUTH_TOKEN = "----------------------------------------------"
# TWILIO_KEY_SID = "----------------------------------------------"
# TWILIO_KEY_AUTH_TOKEN = "----------------------------------------------"

client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
http = httplib2.Http()

def getFirstTumblrPostByTag(tag):
  print(urllib2.quote(tag.encode('utf-8')))
  tagEncoded = urllib2.quote(tag.encode('utf-8'))
  responseTumblr, bodyTumblr = http.request("https://api.tumblr.com/v2/tagged?tag=" + tagEncoded + "&api_key=----------------------------------------------", "GET")

  # print("https://api.tumblr.com/v2/tagged?tag=" + tag + "&api_key=----------------------------------------------")

  try:
    parsed_body_tumblr = json.loads(bodyTumblr)
  except Exception as e:
    print "Unable to parse Tumblr JSON, %s" % (e)

  print(parsed_body_tumblr['response'])
  if parsed_body_tumblr['response'] == []:
    tumblrTagSearchPostURL = 'None Found :('
    return tumblrTagSearchPostURL
  else:
    tumblrTagSearchPostURL = parsed_body_tumblr['response'][0]['post_url']
    return tumblrTagSearchPostURL


def translate(textArray, languageCode):
  "Sends text to Google for translation for the specified language code."

  translatedTexts = [];

  for text in textArray:
    translateURL = "https://www.googleapis.com/language/translate/v2?key=%s&source=en&target=%s&q=" % (GOOGLE_API_KEY, languageCode)
    textEncoded = urllib2.quote(text)
    response, body = http.request(translateURL + textEncoded, "GET")

    try:
      parsed_body = json.loads(body)
    except Exception as e:
      print 'Unable to parse Google JSON'

    # Goal: get translatedText it of the parsed JSON document
    translations = parsed_body['data']['translations']
    firstTranslation = translations[0]
    translatedTexts.append(firstTranslation['translatedText'])

    # print(firstTranslation['translatedText'])

    tumblrPost = getFirstTumblrPostByTag(firstTranslation['translatedText'])

    client.messages.create(
      to="9254007476",
      from_="+14153196608",
      body="\n"+"Untranslated Text: "+text+"\n"+"Translated Text: "+firstTranslation['translatedText'] + "\n" + "First Tumblr Post: " + tumblrPost
    )

  return translatedTexts

print(translate(['doge', 'pepe', 'library', 'cars', 'trump', 'skateboard', 'table', 'chair'], 'fr'))
