# TheMatrix

This web application was created as final project for Beetroot Academy's "Python Development" Course. It represents a taxi app which allows users to place orders, track their status, chat with both current order's driver and administrators of the company and also rate the drivers that they've interacted with. 


## Authors

 - [Eduard Stan](https://github.com/EdyStan)
 - [Oana Sîrbu](https://github.com/Oana4)
 - [Anastasiya Sviderska](https://github.com/anastasiyasviderska)


## Requirements

To continue with the development of this code, one should be up-to-date to all libraries that have been used. They can be easily installed using 

```bash
  pip install -r requirements.txt
```
    
## Description

The main page of our app displays information about who we are, special offers, reviews from our customers/employees regarding the services and also some nice suprises.

When a new user registers in the application, (s)he can choose his role (will (s)he be a driver, or a passenger?) and (s)he will be redirected to the coresponding register page. After registeration, the page will redirect the user to the login part. 

Right after logging in, one will be redirected to the special menu designed with a touch of autenticity for driver/passenger, depending the role that was chosen. 

The friendly interface for passenger menu functionality hides many backend lines of code, that in principle facilitate the following features: place an order/see status of current order, chat with current driver (if exists), open HelpDesk, rate a driver, change your password, see your balance and even add more money to your account. 

On the other side, when accesing his menu, a driver is capable of: see available orders, assign an order and also start the movement (set the order status to "in progress"). Moreover, he can also see his income (that increases with each finished order), chat with his passengers and with administrators. The possibility of changing the account's password exists here, too.

Have we managed to get your attention? If so, test our app and feel free to leave us some advice :)
