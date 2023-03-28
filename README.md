# Greg-Medi-Scrub
Gregmediscrub is a fictional hospital attire store designed and implemented with Django, Python, HTML, and CSS. It aims to provide an easy-to-use interface where customers can browse all items at once or sort into specified categories. The site offers search functionality and an inbuilt stock system to ensure users cannot buy things that are not currently in stock. Once signed in, users can save an address to their profile for easy and convenient checkout.

The deployed site can be visited here: <a href="https://gregmediscrubs.herokuapp.com/" target="_blank">Gregmediscrub</a> for more options.

# Table of Contents
- [Planning Phase](#planning-phase)
    - [Strategy](#strategy)
        - [Site Aims](#site-aims)
        - [Opportunities](#opportunities)
        - [Scope](#scope)
        - [Structure](#structure)
            - [User Stories:](#user-stories)
        - [Skeleton](#skeleton)
            - [Wireframes:](#wireframes)
            - [Database Schema:](#database-schema)
        - [SEO considerations](#seo-considerations)
        - [Content](#content)
        - [Surface](#surface)
    - [Agile Development Process](#agile-development-process)
    - [E-commerce Application Type](#e-commerce-application-type)
    - [Marketing Stratergy](#marketing-stratergy)
- [Features](#features)
    - [Common to All Pages](#Common-to-all-pages)
        - [Navbar](#navbar)
        - [Footer](#footer)
        - [Notifications](#notifications)
    - [Page content](#page-content)
        - [Home Page](#home-page)
        - [Products Page](#product-page)
        - [Product Details Page](#product-detail-page)
        - [Reviews](#reviews)
        - [Edit product - frontend form](#edit-product---frontend-form)
        - [Bag](#bag)
        - [Checkout](#checkout)
        - [Checkout Success](#checkout-success)
        - [Profile](#profile)
        - [Inquiry](#inquiry)
        - [Authentication](#authentication)
        - [Responsive Design](#responsive-design)
- [Admin Panel for Store Admin](#admin-panel-for-store-admin)
    - [Admin Panel Overview](#admin-panel-overview)
        - [Products](#products)
        - [Messages](#messages)
        - [Orders](#orders)
    - [Future Features](#future-features)
- [Testing Phase](#testing-phase)
- [Deployment](#deployment)
- [Technologies used](#technologies-used)
- [Credits](#credits)
- [Media](#media)

---

## PLANNING PHASE
- ### Strategy
    - ### Site-Aims
        The aim of a gregmediscrubs ecommerce store is to provide high-quality, durable, and comfortable medical scrubs to healthcare professionals. The site cater to the needs of medical professionals such as doctors, nurses, and other healthcare staff who require comfortable and practical uniforms for their work.

        Some key goals of the site include:

        1. Offering a wide range of medical scrubs: Provides a diverse range of medical scrubs to cater to the needs of different healthcare professionals. This include scrubs for men, women, and unisex options in various sizes, colors, and styles.

        2. Providing high-quality products: The site aim to offer high-quality medical scrubs that are durable, comfortable, and made from high-quality fabrics.

        3. Ensuring easy navigation: The site is user-friendly and easy to navigate. Customers are be able to find the scrubs they need quickly and easily.

        4. Offering competitive pricing: The store offer competitive pricing to ensure that customers get good value for their money.

        5. Providing excellent customer service: The site aim to provide excellent customer service by responding promptly to customer queries, offering easy returns and exchanges, and ensuring timely delivery of products.

        6. Ensuring secure transactions: The ecommerce store use secure payment gateways and ensure that customer data is protected.

        Overall, the aim of the site provides a hassle-free shopping experience for healthcare professionals looking to purchase medical scrubs.

    - ### Opportunities
        | Opportunities | Importance | Viability/Feasibilty |
        |---------------|-------------|---------------------|
        | Product Filter/search | 5 | 5
        | Account profile | 5 | 5
        | SEO language | 5 | 5
        | stripe payments | 5 | 5
        | User feedback for actions taken | 5 | 5
        | Check out system | 5 | 5
        | Guest checkout completion | 5 | 5
        | User login/register | 5 | 5
        | Delivery information | 5 | 5
        | User Role permissions | 5 | 5
        | Product reviews | 5 | 3
        | Full CRUD functionality | 5 | 5
        | Order History | 5 | 5
        | Stock management system | 5 | 3
        | Contact form | 3 | 5
        | Social Media pages | 5 | 5
        | Promotions and adverts | 3 | 3
        | Password Recovery| 5 | 5
        | Email confirmation of order | 5 | 5
        | Related products | 1 | 1
        | Saved customer details on checkout | 5 | 5
        | Admin can add/remove products via the front end	 | 3 | 5
        | Multiple currencies | 5 | 1
        | Terms and conditions | 3 | 5
        | Guest checkout completion | 5 | 5
        | Generate sales reports | 5 | 1
        | Order Status | 2 | 5
        | Ability to edit order until status set to processing | 1 | 5
        | Store blog | 1 | 5
        | Full CRUD functionality | 5 | 5
        | ----- | ----- | -----
        | Total| 127 | 132

    - ### Scope
    - ### Structure
        - ### User Stories:
            - EPIC 1 - Set up and Deployment:

            - EPIC 2 - Viewing and Navigation:

            - EPIC 3 - Registration and User Accounts:

            - EPIC 4 - Product browsing Search:
                - As a shopper, I want to be able to search for products by entering keywords or by brand so that I can easily find what I am looking for
                - As a shopper, I want to be able to see high-quality product images and descriptions when I search for product so that I can make an informed purchase decision
                - As a shopper, I want to be able to sort my search by relevance, price, popularity so that I can find the product that is best for me

            - EPIC 5 - Shopping cart and Checkout:
                - As a shopper, I want to be able to easily add products to my cart so that I can keep track of the items I want to purchase
                - As a shopper, I want to be able to view the content of my cart and see the total cost of my purchase so that I can make sure I have everything I need before checkout
                - As a shopper, I want to be able to adjust the quantity of items in my cart so that I can control how many of each product I want to buy
                - As a shopper, I want to be able to remove items from my chart so that I can change my mind about a purchase
                - As a shopper, I want to be able to select a payment option so that I can pay for the items I want to purchase

            - EPIC 6 - Site Admin and Store Management:
                - As site admin, I want to be able to track and manage my inventory levels, so that I can prevent stockouts and ensure that I have enough product to meet customer demand
                - As a site admin, I want to easily manage and update product information, so that I can keep my online store up-to-date
                - As site admin, I want to be able to view and manage customer orders and shipping information, so that I can keep track of my sales.

            - EPIC 7 - Product Reviews and Product detail Page:
                - As a shopper, I want to be able to view high-quality product images so that I can get a good look at the product before purchase
                - As a shopper, I want to be able to see product details such as the size, weight, color and materials so that I can make informed purchase decision.
                - As a shopper, I want to be able to add the product to my cart so that I can purchase it quickly
                - As a customer, I want to be able to review products and give feedback after my purchase

            - EPIC 8 - User Account Management:
                - As a user, I want to be able to sign up for an account so that I can easily track my orders and save my information for future purchases.
                - As a user, I want to be able to log in to my account so that I van access my saved order history
                - As a user, I want to be able to reset my password if I forget so that I can regain access to my account
                - As a user, I want to be able to update my account information (such as name and address etc), so that my information is always up-to-date
                - As a user, I want to be able to view my order history so that I can keep track of all my purchases
    - ### Skeleton
        - ### Wireframes
                - Home Page:
                - Products Page:
                - Product Details Page
                - Shopping Bag Page:
                - Checkout Page:
                - User Profile Page:
                - Order Confirmation Page:
        - ### Database Schema:
                - All Products Table
                - Product Reviews Table
                - Contact us Table
                - Order Tables
                - Profile Table
                - Full ERD from PgAdmin
    - ### SEO considerations
        - Keywords
            - The following keywords were used for the website for optimazation; medical scrubs, scrub uniforms, nursing scrubs, medical uniforms, scrub tops, scrub pants, scrub sets, petite scrubs, tall scrubs, plus size scrubs, maternity scrubs, medical lab coats, dental scrubs, veterinary scrubs, surgical scrubs, healthcare scrubs, hospital scrubs, nursing shoes, compression socks, medical accessories
        - Page Titles
        - Robots.txt and sitemap.xml
    - ### Content
    - ### Surface
        - Colour Scheme
        - Typography
- ### Agile Development Process
- ### E-commerce Application Type
- ### Marketing Stratergy
- ## Features
    - ### Common to All Pages
        - ### Navbar
            - Overall Appearance
                - Desktop
                - Mobile
            - Common Navbar Features for both Desktop and Mobile
                - Logo
                    - Desktop
                    - Mobile
                - Search Bar
                    - Desktop
                    - Mobile
            - Account menu
                - Unauthenticated
                - Authenticated
            - Bag icon
        - ### Footer
            - Desktop
            - Mobile
            - Common Features to both Desktop and Mobile
                - Social Media Links
                     <img width="1440" alt="Gmw facebook buisness page" src="https://user-images.githubusercontent.com/69070044/227708744-9e11349a-ef2e-4501-a58b-5066f740cebb.png">
                - Newsletter Sign Up
                - Sitemap
        - ### Notifications
    - ### Page content
        - ### Home Page
        - ### Products Page
        - ### Product Details Page
        - ### Reviews
            - Unauthenticated
            - Authenticated
        - ### Edit product - frontend form
        - ### Bag
            - Desktop
            - Mobile
        - ### Checkout
            - Desktop
            - Mobile
        - ### Checkout Success
        - ### Profile
        - ### Inquiry
        - ### Authentication
        - ### Responsive Design
- ## Admin Panel for Store Admin
    - ### Admin Panel Overview
        - ### Products
        - ### Messages
        - ### Orders
    - ### Future Features
        - Product size
        - Sales reports
        - Additional payment methods
        - Additional user account features
        - Product options
        - Ticketing Sytem
- ## Testing Phase
- ## Deployment
- ## Technologies used
- ## Credits
- ## Media