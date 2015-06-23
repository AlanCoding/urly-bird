<<<<<<< HEAD
# URLy Bird

## Description

Create a URL shortener/bookmarking site with Django.
=======
# URLy Bird API

## Description

Add a REST-based API to [URLy Bird](https://github.com/tiyd-python-2015-05/urly-bird).
>>>>>>> d8bd4943cabe5be5d78554a315a43751f24277ca

## Objectives

### Learning Objectives

After completing this assignment, you should be able to:

<<<<<<< HEAD
* Extrapolate from current Django projects to build a new project of substantial size and features
* Determine which model field types to use to represent data
* Translate English descriptions of data queries into Django ORM queries
* Use PostgreSQL to store Django data
* Make use of Bootstrap and hand-written CSS to style your application
* Select generic views from Django to speed development
* Generate charts via Django views
* Protect access and choose behavior based on user status
=======
* Design a simple REST API.
* Implement authentication and authorization for an API in Django.
>>>>>>> d8bd4943cabe5be5d78554a315a43751f24277ca

## Details

### Deliverables

<<<<<<< HEAD
* A Git repo called urly-bird containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * a Django project

### Requirements  

* No PEP8 or Pyflakes warnings or errors

## Normal Mode

Create a Django project for a bookmarking site. Users can save URLs with
a title and an optional description.

Each bookmark should have a unique code -- something like "x1yrd3a" -- for use
in looking it up later. Create a route like "/b/{code}" that will redirect any
user -- not just logged in users -- to the bookmark associated with that code.
The route does not have to look just like the example.

When a user -- anonymous or logged in -- uses a bookmark URL, record that user,
bookmark, and timestamp. A suggested name for this model is Click, even though
you can navigate to the URL without a click by entering it in your navigation
bar.

The site should have user registration, login, and logout.

On a logged in user's index page, they should see a list of the bookmarks
they've saved in reverse chronological order, paginated. The bookmark links
should use the internal short-code route, not the original URL. From this page,
they should be able to edit and delete bookmarks.

A user's bookmark page should be public. When viewing a user's bookmark page
when not that user, the links to edit and delete bookmarks should not show up.

There should also be a page to view all bookmarks for all users in reverse
chronological order, paginated.

These features are restated in the following list:

* Users can create an account, log in, and log out.
* Users can save a URL as a bookmark with a title and an optional description.
* Users can see all their bookmarks in a paginated list in reverse chronological order.
* Users can edit and delete their own bookmarks.
* Users can see all the bookmarks for another user in a paginated list in reverse chronological order.
* Users can see all the bookmarks for all users in a paginated list in reverse chronological order.
* Users can access a bookmark through a URL with a short code, allowing them to share bookmarks.
* When a user accesses a bookmark, the access is recorded with the bookmark, the user -- or anonymous user -- and the timestamp.

Once you have all these features, you will need to generate a good amount of
click data. Create fake data for this. Numpy and Faker are useful libraries for
creating your fake data.

Add a stats page for each link where you can see the traffic for that link for the last 30 days in a line chart.

Add an overall stats page for each user where you can see a table of their links by popularity and their number
of clicks over the last 30 days. This page should only be visible to that user.
=======
Instead of forking this repo, use your previous URLy Bird project and push there.

## Normal Mode

Add an API under the URL `/api` to URLy Bird.

This API should be read-only unless the user is authenticated. If authenticated,
the user can add new bookmarks and edit and delete their own bookmarks.

The API should allow for:

* Viewing, editing, and deleting bookmarks
* Seeing the click stats for a bookmark
* Adding a click to a bookmark
* Allowing a user to see their overall stats (This is a replication of the
  overall stats page from the original assignment.)
>>>>>>> d8bd4943cabe5be5d78554a315a43751f24277ca

## Hard Mode

For hard mode, do everything shown above, plus any of the following features.

<<<<<<< HEAD
* Allow users to create topical lists of URLs, with each list having a title and
optional description.
* Allow resorting of URLs on topical list pages.
* Allow users to add [tags](https://en.wikipedia.org/wiki/Tag_(metadata)) to their URLs and have pages for each user + tag combo, as well as overall tag pages.
* On individual link stats pages, make a table of where the clicks for your links are coming from by country. Bonus -- display this on a map.
* Add an option to the individual and group stats pages where you can see stats for the last week, last 30 days, last year, or all time.
* Add functional tests for all your pages.

## Additional Resources

* [Hashids](http://hashids.org/python/). These may be useful for creating short URLs.
=======
* Allow new user creation through the API.
* Allow token-based authentication.
* Support topical lists or tags from the original assignment through the API.
* Add functional tests for your API.
>>>>>>> d8bd4943cabe5be5d78554a315a43751f24277ca
