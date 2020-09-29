import json
import pymsteams
from config.settings import config


def send_teams_message(message, title=None, button_text=None, button_link=None):
    """
    Send message to Microsft Teams channel via webhook
    """
    myTeamsMessage = pymsteams.connectorcard(config['TEAMS']['WEBHOOK_URL'])
    if title is not None:
        myTeamsMessage.title(title)
    if button_text is not None and button_link is not None:
        myTeamsMessage.addLinkButton("This is the button Text", "https://github.com/rveachkc/pymsteams/")
    myTeamsMessage.text(message)
    result = myTeamsMessage.send()
    return result


def send_teams_card_message(title, activity_title, activity_subtitle=None, activity_image=None, activity_text=None,
                            facts=None, section_text=None, section_image=None, section_image_title=None):
    myTeamsMessage = pymsteams.connectorcard(config['TEAMS']['WEBHOOK_URL'])
    # create the section
    myMessageSection = pymsteams.cardsection()
    myMessageSection.title(title)

    # Activity Elements
    if activity_title is not None:
        myMessageSection.activityTitle(activity_title)
    if activity_title is not None:
        myMessageSection.activitySubtitle(activity_subtitle)
    if activity_title is not None:
        myMessageSection.activityImage(activity_image)
    if activity_title is not None:
        myMessageSection.activityText(activity_text)

    # Facts are key value pairs displayed in a list.
    if len(facts) != 0:
        for fact in facts:
            myMessageSection.addFact(fact['name'], fact['value'])

    # Section Text
    myMessageSection.text(section_text)

    # Section Images
    if section_image != 'False':
        myMessageSection.addImage(section_image, ititle=section_image_title)

    # Add your section to the connector card object before sending
    myTeamsMessage.addSection(myMessageSection)
    myTeamsMessage.summary("Flask-API automatic message")

    myTeamsMessage.printme()

    return myTeamsMessage.send()


def send_teams_test_message():
    myTeamsMessage = pymsteams.connectorcard(config['TEAMS']['WEBHOOK_URL'])
    # create the section
    myMessageSection = pymsteams.cardsection()

    # Section Title
    myMessageSection.title("Section title")

    # Activity Elements
    myMessageSection.activityTitle("my activity title")
    myMessageSection.activitySubtitle("my activity subtitle")
    myMessageSection.activityImage("http://i.imgur.com/c4jt321l.png")
    myMessageSection.activityText("This is my activity Text")

    # Facts are key value pairs displayed in a list.
    myMessageSection.addFact("this", "is fine")
    myMessageSection.addFact("this is", "also fine")

    # Section Text
    myMessageSection.text("This is my section text")

    # Section Images
    myMessageSection.addImage("http://i.imgur.com/c4jt321l.png", ititle="This Is Fine")

    # Add your section to the connector card object before sending
    myTeamsMessage.addSection(myMessageSection)
    myTeamsMessage.summary("Test Message")

    myTeamsMessage.printme()

    result = myTeamsMessage.send()
    return result
