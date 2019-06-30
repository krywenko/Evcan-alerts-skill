Weather alert skill for mycroft
this weather alert  works with enviroment canada  in the mycroft configuration page ( or edit setting.json)
just add your weather zone  - https://weather.gc.ca/canada_e.html  goto to your province and click on ATOM 
example sioux lookout
https://weather.gc.ca/city/pages/on-135_e.html   you need this on-135_e
then go to the public alert page click on the image where your province is and then region  for your regiom click on ATOM 
https://weather.gc.ca/warnings/index_e.html
https://weather.gc.ca/rss/battleboard/on2_e.xml  you need this on2_e as a code

the skill works with my mycroft TFT screen ( https://github.com/krywenko/TFT-ifterface-for-Mycroft-AI) but is not required.     for  sever warnnings Ie: tornados  house wreck winds, hurricane  etc..   it wiil sound an alarm and then say the event
for less severe such as thunder storms  it will  display on the TFT screen and give mild cue of thunder sound  for  heavy rain it gives a  rain cue.  for other one a simple bleep..
 you can then ask what the alert is by saying  "weather alerts"  "what are the weather alerts' or "any weather alerts" and it will read the description of the alert and give the current condition and the events forcast 
