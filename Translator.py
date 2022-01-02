"""
Function to translate from English to French
"""
# Import dependencies
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def englishtofrench(recognized_text):
    """Function to translate from English to French"""

    #Define authentication components in order to use IBM Watson Language Translator
    url = 'https://api.us-south.assistant.watson.cloud.ibm.com/instances/59c12ded-746f-4d31-a5e8-376f91672a3f'
    api_key = 'RvtqoUuB-D_ZSJ3DMCo6RDwoZhQ5MsVoIOsWC3uNig7o'
    version = '2018-05-01'

    #Creating the language translator object
    authenticator = IAMAuthenticator(api_key)
    language_translator = LanguageTranslatorV3(version=version, authenticator=authenticator)
    language_translator.set_service_url(url)

    #Create the actual translated response as a string
    fr_translation_response = language_translator.translate(\
        text=recognized_text, model_id='en-fr')
    fr_translation=fr_translation_response.get_result()

    return list(fr_translation.items())[0][1][0]['translation']

  def english_to_french(english_text):
    '''
    Convert a string of english text to a string of french text
    '''
    if isinstance(english_text, str):
        try:
            req = language_translator.translate(text=english_text,
                model_id='en-fr')
            return req.get_result()['translations'][0]['translation']
        except:
            return 'No Translation Found'
    else:
        return "Not a valid input"

def french_to_english(french_text):
    '''
    Convert a french to english text
    '''
    if isinstance(french_text, str):
        try:
            req = language_translator.translate(text=french_text,
                model_id='fr-en')
            return req.get_result()['translations'][0]['translation']
        except:
            return "Error"
    else:
        return "Invalid entry"
