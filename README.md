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
        Due to limited timeframe for this project and the specific grading criteria, it will be necessary to make additional compromises during the design and development phases. To address this, I will employ an agile methodology and conduct weekly progress reviews. Based on the results of these reviews, I will make decisions about which features to include, modify, or remove in order to meet the deadline and deliver a viable minimum viable product (MVP).

        To prevent the project from expanding beyond its original scope, I have implemented the MoSCoW method to categorize the various requirements according to their importance. This will enable me to prioritize the most critical elements and ensure that I can achieve my ultimate objective of delivering a fully functional MVP by the established deadline.: -

        To create a minimum functional E-commerce site, UX efforts must address these opportunities: -
        - Full CRUD Functionality.
        - User login/register.
        - Checkout system.
        - Account profile.
        - Mailing list.
        - Product Filters/searching.
        - Stripe payments.
        - SEO language throughout.
        - Guest checkout completion.
        - User Role permissions.
        - Order History.
        - Social Media page.
        - Password Recovery.
        - Email confirmation of order.
        - User feedback for actions taken.
        - Saved customer details on checkout.

        To enhance the customer experience and increase the sites functionality, UX efforts should address these opportunities: -
        - Product reviews.
        - Contact form.
        - Admin can add/remove products via the front end.
        - Delivery information.
        - Terms and conditions.

        To increase the sites popularity and customer base, UX efforts could address these opportunities: -
        - Site advert/promotion.
        - Video demo of products.
        - Related products
        - Ability to edit order until status set to processing.
            
        As they are so far out of the scope of this project, UX efforts will not address these opportunities: -
        - Multiple currencies.
        - Generate sales reports.

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
            The Balsamiq wireframing tool was utilized to create visual representations of the website's design and functionality. The wireframes utilized in the layout planning process are provided below. Nonetheless, certain alterations or eliminations were made during the development phase due to limitations of time or feasibility.
            - Home Page:
            - Products Page:
            - Product Details Page
            - Shopping Bag Page:
            - Checkout Page:
            - User Profile Page:
            - Order Confirmation Page:
        - ### Database Schema:
            - The database table scheme was created using <a href="https://drawsql.app/" target="_blank">drawsql.app</a> and can be seen below.
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
        Due to the nature of the site, there were limited opportunities for textual content. As many of the keywords were product-related, I focused on utilizing heading and semantic tags effectively to ensure a high-quality search rating.
    - ### Surface
        After planning the project, selecting an appropriate theme became the next step. While aiming for simplicity, I incorporated color to enhance the site's visual appeal. To maintain a clean and user-friendly design, I employed ample white space throughout.
        - Colour Scheme
            - Although black and white served as the primary colors on the site, I added additional hues to highlight important content and establish a distinct brand identity. The accompanying color grid guided my selection process, although some initial ideas had to be altered based on contrast considerations, which are outlined below.
        - Typography
            - <a href="https://fonts.google.com/specimen/DM+Sans?query=dm+s" target="_blank">DM Sans</a> was utilized for the primary headings and logo, this font is clean and straightforward, ensuring legibility while also making a bold statement.
- ### Agile Development Process
- ### E-commerce Application Type
    - Our platform operates on a Business-to-Customer (B2C) model, enabling medical professionals to easily purchase high-quality scrubs at competitive prices from the comfort of their homes or workplaces. This website is designed to be user-friendly, with a streamlined interface that allows customers to browse and purchase products with ease. Our product catalogue features a wide range of medical scrubs in various colors and sizes, ensuring that our customers can find the perfect fit for their unique needs. To make the shopping experience more convenient, we offer secure payment options, fast shipping, and hassle-free returns. Our platform is also optimized for mobile use, enabling customers to access the site on-the-go from any device.
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
                     <img width="1440" alt="Gmw facebook buisness page" src="https://user-images.githubusercontent.com/69070044/229380888-b6bef8b7-410b-4c22-856c-9b8260651f5a.png">
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