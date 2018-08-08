***Superuser information***
username: admin
password: a1234567

This app lets a user add a park from the National Park Service (NPS) to their "passport," see a detailed description of the park,
see reviews of the park, and add friends (which lets them directly see their friends reviews). It is built using Python/Django, with
Javascript for pop-up boxes and CSS for a cleaner look-and-feel.

The Python functions are commented on in the code, but, in summary, they allow users to:

-- Sign-up (def signup), login (def login_view), and logout (def logout_view)

-- Add parks to their "passport" (def your_passport)

-- Once a park is in the passport, they can click to see a more detailed description of the park (JS), see reviews of the park (JS),
add their own review (def submit_revew), and remove it from their passport (def remove_from_passport).

-- They can add a friend from the list of users (def add_friend) and click on their friends to see their reviws (JS).

The biggest thing I could not figure out that I kept struggling with was Python's messages when returning a redirect/reverse.
You can see the code I left in for it views.py (which should render the templare in your_passport.html) and one attempt that does not
render the message in the error message of add_park_information. The code doesn't throw me any error and otherwise functions (the
page reloads, just without the message being passed back), so I am not sure how to troubleshoot it.

I didn't make direct calls to the NPS API because I kept getting a 403 error -- I understand that I am getting it because the NPS site
is trying to block automatic scrapping (https://airbrake.io/blog/http-errors/403-forbidden-error), but I am not 100% sure how to
"distinguish" my call so that doesn't happy; since I was able to access the information, I just downloaded it into the park_data.json
file.

Modal box CSS adopted from W3 Schools (though I re-did the Javascript code): https://www.w3schools.com/howto/howto_css_modals.asp

Accordion opener/closer Javascript adopted from W3 Schools: https://www.w3schools.com/howto/howto_js_accordion.asp