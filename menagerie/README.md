# Complete application with authentication, forms, and models

## Goals

Develop a small application that uses `Flask-Login`, `Flask-SQLAlchemy`, and `Flask-WTF` to maintain user sessions and protect some resources within the application.

`menagerie_simple` is an alternative implementation that does not use extensions.

## Outcomes

An application with the following functionality:

- Registration (signup), authentication (login), and update (profile) forms and routes.
- Only authenticated users can adopt/reject animals.
- Locations are hidden for anonymous users.
- Popularity (based on number of adoptions) is shown to anonymous users

## Demo

Use the following command to run the application:

```bash
flask --app menagerie_easy run
```

Alternative:

```bash
flask --app menagerie_simple run
```

## References

- [Flask-Login — Flask-Login 0.6.3 documentation](https://flask-login.readthedocs.io/en/0.6.3/)
- [Flask-WTF — Flask-WTF Documentation (1.2.x)](https://flask-wtf.readthedocs.io/en/1.2.x/)
- [WTForms — WTForms Documentation (3.1.x)](https://wtforms.readthedocs.io/en/3.1.x/)
- [Quick Start — Flask-SQLAlchemy Documentation (3.1.x)](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/)
- [How To Add Authentication to Your App with Flask-Login | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)
- [How to Perform User Authentication with Flask-Login — SitePoint](https://www.sitepoint.com/flask-login-user-authentication/)
