"""***
MIT License

Copyright (c) [2023] [DAXX TEAM]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.***
"""

import requests
from DAXXMUSIC import app
from pyrogram import filters


@app.on_message(filters.command("fake"))
async def address(_, message):
    query = message.text.split(maxsplit=1)[1].strip()
    url = f"https://randomuser.me/api/?nat={query}"
    response = requests.get(url)
    data = response.json()

    if "results" in data:
        user_data = data["results"][0]


        name = f"{user_data['name']['title']} {user_data['name']['first']} {user_data['name']['last']}"
        address = f"{user_data['location']['street']['number']} {user_data['location']['street']['name']}" 
        city = user_data['location']['city']
        state = user_data['location']['state']
        country = user_data['location']['country'] 
        postal = user_data['location']['postcode']
        email = user_data['email']
        phone = user_data['phone']
        picture_url = user_data['picture']['large']


        caption = f"""
﹝⌬﹞**ɴᴀᴍᴇ** ⇢ {name}
﹝⌬﹞**ᴀᴅᴅʀᴇss** ⇢ {address}
﹝⌬﹞**ᴄᴏᴜɴᴛʀʏ** ⇢ {country}
﹝⌬﹞**ᴄɪᴛʏ** ⇢ {city}
﹝⌬﹞**sᴛᴀᴛᴇ** ⇢ {state}
﹝⌬﹞**ᴘᴏsᴛᴀʟ** ⇢ {postal}
﹝⌬﹞**ᴇᴍᴀɪʟ** ⇢ {email}
﹝⌬﹞**ᴘʜᴏɴᴇ** ⇢ {phone}

       """

random_user_api_url = 'https://randomuser.me/api/'


@app.on_message(filters.command("fake", prefixes="/"))
def generate_fake_user_by_country(client, message):
    country_name = message.text.split("/fake ", maxsplit=1)[1]
    
    # Call the RandomUser API to get fake user information for the specified country
    response = requests.get(f'{random_user_api_url}?nat={country_name}')
    
    if response.status_code == 200:
        user_info = response.json()['results'][0]
        # Extract user details
        first_name = user_info['name']['first']
        last_name = user_info['name']['last']
        email = user_info['email']
        country = user_info['location']['country']
        state = user_info['location']['state']
        city = user_info['location']['city']
        street = user_info['location']['street']['name']
        zip_code = user_info['location']['postcode']
        # Reply with the generated fake user information for the specified country
        message.reply_text(f"𝗡𝗔𝗠𝗘➪ {first_name} {last_name}\n\n𝗘𝗠𝗔𝗜𝗟➪ {email}\n\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬➪ {country}\n\n𝗦𝗧𝗔𝗧𝗘➪ {state}\n\n𝗖𝗜𝗧𝗬: {city}\n\n𝗔𝗗𝗗𝗥𝗘𝗦𝗦:➪{street}\n\n𝗭𝗜𝗣 𝗖𝗢𝗗𝗘➪ {zip_code}")
    else:
        message.reply_text(f"Failed to generate fake user information for {country_name}.")
