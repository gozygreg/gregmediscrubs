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
            ![WireframeHomePageDesktop](https://user-images.githubusercontent.com/69070044/229642008-2451aa1b-7608-4b36-a5a4-1dc703cd0b07.jpg)
            - Products Page:
            ![WireframeProductpageDesktop](https://user-images.githubusercontent.com/69070044/229642474-ecfae5b0-4e67-4a20-8f7e-27d71ddb4131.jpg)
            - Product Details Page
            ![WireframeProductDetailDeskstop](https://user-images.githubusercontent.com/69070044/229642504-655f87ed-84ae-42c8-8645-53e74dd53e30.jpg)
            - Checkout Page:
            ![WireframeCheckoutDesktop](https://user-images.githubusercontent.com/69070044/229642533-df41d14f-b998-461e-8d96-f6e42d007524.jpg)
            - User Profile Page:
            ![WireframeProfilepageDesktop](https://user-images.githubusercontent.com/69070044/229642555-21f1433d-96a3-4031-9ba2-32fa83b915f2.jpg)
            - Testimonial List Page:
            ![WireframeTestimonilalistDesttop](https://user-images.githubusercontent.com/69070044/229642598-c59531b8-a123-458e-9769-d377825938d4.jpg)
            - Testimonial Detail Page:
            ![WireframeTestinonialDetailDesktop](https://user-images.githubusercontent.com/69070044/229642610-8628de48-3648-4c4b-a461-b0b70c1ef80f.jpg)
            - Inquiry Page:
            ![WireframeInquiryDesktop](https://user-images.githubusercontent.com/69070044/229642579-8f6cd851-c872-4950-b68b-7942e6e76966.jpg)
        - ### Database Schema:
            - The database table scheme was created using <a href="https://drawsql.app/" target="_blank">drawsql.app</a> is explained below.
                - A Category can have multiple Products, but a Product belongs to only one Category. This is represented by a one-to-many relationship between Category and Product.
                - A Product can have multiple ReviewRatings, and each ReviewRating is associated with one Product and one User. This is represented by a many-to-one relationship between Product and ReviewRating, and a many-to-one relationship between User and ReviewRating.
                - A User can have multiple Testimonials, but each Testimonial is associated with one User. This is represented by a one-to-many relationship between User and Testimonial.
                - A User can have one UserProfile, but each UserProfile is associated with one User. This is represented by a one-to-one relationship between User and UserProfile.
                - A CustomerInquiry can have multiple InternalCommunicationNotes, but each InternalCommunicationNotes is associated with only one CustomerInquiry. This is represented by a one-to-many relationship between CustomerInquiry and InternalCommunicationNotes.
                - An Order can have multiple OrderLineItems, and each OrderLineItem is associated with one Order and one Product. This is represented by a many-to-one relationship between Order and OrderLineItem, and a many-to-one relationship between Product and OrderItem. An Order is associated with one UserProfile, but a UserProfile can be associated with multiple Orders. This is represented by a many-to-one relationship between UserProfile and Order.
                - Full ERD from PgAdmin: <a href="https://drawsql.app/teams/greg-7/diagrams/erd-gregmediscrubs" target="_blank">Database Models</a> 
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
            - Desktop
            <img width="1000" alt="header-dv" src="https://user-images.githubusercontent.com/69070044/230581318-efc69a72-d44e-464f-b27d-69a3ec7b9ad1.png">
            - Mobile
            <img width="350" alt="header-mv" src="https://user-images.githubusercontent.com/69070044/230581479-7c1f888a-4c9b-4f78-ac5d-0f091a4090a5.png">
            <img width="350" alt="nav-bar-mobile" src="https://user-images.githubusercontent.com/69070044/230593234-6a8c9d0c-468b-4bd9-beaf-74fedea20979.png">
            - Account menu
                - Unauthenticated
                <img width="350" alt="account-unauthenticated" src="https://user-images.githubusercontent.com/69070044/230594669-08f62c1a-ae3a-4a5b-95d9-c9d2ec17e378.png">
                - Authenticated
                <img width="350" alt="account-authenticated" src="https://user-images.githubusercontent.com/69070044/230594622-c786b2f1-fdae-4cdc-8ccf-6721e3ad1440.png">
                - Super User/Admin
                <img width="1000" alt="account-superuser" src="https://user-images.githubusercontent.com/69070044/230593240-4c981742-36d6-4c69-97d7-dbcc331e0f48.png">
            - Bag icon
            <img width="350" alt="bag-icon" src="https://user-images.githubusercontent.com/69070044/230593254-d9cb1094-c815-4ddb-8289-fe8972df879a.png">
            - Message notifications
            <img width="350" alt="message notifications-mv" src="https://user-images.githubusercontent.com/69070044/230593236-1ba101a8-21cb-4963-b476-5a1e5ac54504.png">
            <img width="1000" alt="message-notification-dv" src="https://user-images.githubusercontent.com/69070044/230593239-b46e21e4-f262-4c46-b7e0-fbf586bb4588.png">


        - ### Footer
            - Desktop
            <img width="1000" alt="footer-dv" src="https://user-images.githubusercontent.com/69070044/230580535-1f75190e-8e26-41fd-b9da-8df423024abe.png">
            - Mobile
            <img width="350" alt="footer-mv" src="https://user-images.githubusercontent.com/69070044/230580574-612edad8-1885-4487-a355-fd5d2e120ea4.png">
            - Common Features to both Desktop and Mobile
                - Social Media Links
                     <img width="1000" alt="Gmw facebook buisness page" src="https://user-images.githubusercontent.com/69070044/229380888-b6bef8b7-410b-4c22-856c-9b8260651f5a.png">
                - Newsletter Sign Up
                - Sitemap
                <img width="1000" alt="sitemap" src="https://user-images.githubusercontent.com/69070044/230581556-281d205b-7f16-4a7c-81b7-b2b2f019c581.png">
        - ### Notifications
    - ### Page content
        - ### Home Page
            - Desktop
            <img width="1000" alt="home-page-dv" src="https://user-images.githubusercontent.com/69070044/230580158-a3709679-0626-46bf-9341-d205fc07a247.png">
            - Mobile
            <img width="350" alt="home-page-mv" src="https://user-images.githubusercontent.com/69070044/230580185-d7d480eb-e457-4504-aeb6-0d81136ea137.png">
        - ### Products Page
            - Desktop
            <img width="1000" alt="product-page-dv" src="https://user-images.githubusercontent.com/69070044/230580465-4369af91-7566-4fef-bcb2-d299c297e4db.png">
            - Mobile
            <img width="350" alt="product-page-mv" src="https://user-images.githubusercontent.com/69070044/230580495-cec54dcd-38e5-4143-b95b-ece44d2efc25.png">
        - ### Product Details Page
            - Desktop

            - Mobile
            <img width="350" alt="product-detail-mv" src="https://user-images.githubusercontent.com/69070044/230593253-f3efcba2-6483-41cb-80f9-4205ff0966d7.png">
        - ### Reviews
            Only authenticated users that have purchased a product can review the product.
            - Desktop
            <img width="1000" alt="reviews-section-dv" src="https://user-images.githubusercontent.com/69070044/230580773-d0b1826e-9447-45c0-9e92-2147356379a0.png">
            - Mobile
            <img width="350" alt="reviews-section-mv" src="https://user-images.githubusercontent.com/69070044/230580810-78882c5a-68af-479d-a8b8-47b6563cf0a9.png">
        - ### Edit product - frontend form
            Only site admin have access to edit or delete a product. Below is the product edit from
            <img width="1000" alt="product-edit-page" src="https://user-images.githubusercontent.com/69070044/230597856-d189e0ad-a49f-4db6-b237-380c543b55b5.png">
        - ### Bag
            - Desktop
            <img width="1000" alt="bag-page-dv" src="https://user-images.githubusercontent.com/69070044/230580233-93f2f331-358b-4aae-9dec-aabe088cbe40.png">
            - Mobile
            <img width="350" alt="bag-page-mv" src="https://user-images.githubusercontent.com/69070044/230580251-fae07268-7995-498c-a277-f32e77a5a02b.png">
        - ### Checkout
            - Desktop
            <img width="1000" alt="checkout-dv" src="https://user-images.githubusercontent.com/69070044/230593246-09f3b193-0695-49ea-80b3-cb13ab21501e.png">
            - Mobile
            <img width="350" alt="checkout-mv" src="https://user-images.githubusercontent.com/69070044/230593244-a652c26c-b96d-4077-b3cc-c5dd15d55467.png">
        - ### Checkout Success
            - Desktop
            <img width="1000" alt="checkout-success-dv" src="https://user-images.githubusercontent.com/69070044/230593250-8e24d952-7315-4551-a884-018c95293814.png">
            - Mobile
            <img width="350" alt="checkout-success-mv" src="https://user-images.githubusercontent.com/69070044/230593247-ab684c44-1d0e-48b3-80bc-fd5358567a9d.png">
        - ### Checkout Success
        - ### Testimonial
            - ## Testimonial list
                - Desktop
                <img width="1000" alt="testimonial-list-dv" src="https://user-images.githubusercontent.com/69070044/230580860-a6deee2a-03f7-43b5-9bf2-b99997a45a8d.png">
                - Mobile
                <img width="350" alt="testimonial-list-mv" src="https://user-images.githubusercontent.com/69070044/230580896-44763bda-f845-420e-8c4c-a66adfd5febc.png">
            - ## Testimonial detail
                - Desktop
                <img width="1000" alt="testimonial-detail-dv" src="https://user-images.githubusercontent.com/69070044/230580942-8ed898a1-539b-47d6-8f21-4301defb3e03.png">
                - Mobile
                <img width="350" alt="testimonial-detail-mv" src="https://user-images.githubusercontent.com/69070044/230580971-69089bb0-eb2d-4087-a803-249b0a7b259b.png">
        - ### Profile
            - Desktop
            <img width="1000" alt="profile-page-dv" src="https://user-images.githubusercontent.com/69070044/230580048-7505a087-8d55-44a0-9286-3d45779e838b.png">
            - Mobile
            <img width="350" alt="profile-page-mv" src="https://user-images.githubusercontent.com/69070044/230580091-a6851079-52d6-4a73-8465-be987fbf4939.png">
            - Signup
                - Desktop
                <img width="1000" alt="signup-dv" src="https://user-images.githubusercontent.com/69070044/230595988-eeb0a1d1-0f50-4e42-8e4d-b581059c34bd.png">
                - Mobile
                <img width="350" alt="signup-mv" src="https://user-images.githubusercontent.com/69070044/230595985-c340987f-4bff-4b63-b952-0860672f72e7.png">
            - Sign In
                - Desktop
                <img width="1000" alt="signin-dv" src="https://user-images.githubusercontent.com/69070044/230595989-6f02134e-6402-40a4-a66f-371e4508a669.png">
                - Mobile
                <img width="350" alt="signin-mv" src="https://user-images.githubusercontent.com/69070044/230595991-ae5e5084-4e4f-47f8-bf6f-133291629109.png">
            - Sign Out
                - Desktop
                <img width="1000" alt="signout-page-dv" src="https://user-images.githubusercontent.com/69070044/230580308-1c6f236e-20d3-47e6-ba9e-1c4421b4087e.png">
                - Mobile
                <img width="350" alt="signout-page-mv" src="https://user-images.githubusercontent.com/69070044/230580351-018b70a7-6f0f-4386-86e8-5b9b21aaf4fb.png">
        - ### Inquiry
            - Desktop
            <img width="1000" alt="inquiry-page-dv" src="https://user-images.githubusercontent.com/69070044/230580397-35194ef1-21fa-46aa-bef9-418c1efa3ebe.png">
            - Mobile
            <img width="350" alt="inquiry-page-mv" src="https://user-images.githubusercontent.com/69070044/230580418-b4d011e0-8e13-48d9-af30-42c15a6e3ae1.png">
        - ### Authentication
        - ### 404 Page
            - <img width="1000" alt="404" src="https://user-images.githubusercontent.com/69070044/230581541-d4885d67-6888-4627-85f8-664c95ae0316.png">
        - ### Responsive Design
- ## Admin Panel for Store Admin
    - ### Admin Panel Overview
        - ### Products
            - Desktop
            <img width="1000" alt="product-mgt-dv" src="https://user-images.githubusercontent.com/69070044/230580619-762247d4-b930-4c57-97af-83dcec9094c8.png">
            <img width="1191" alt="product-mgt2-dv" src="https://user-images.githubusercontent.com/69070044/230580693-601cff94-cd39-476d-9e51-660a987c6cee.png">
            - Mobile
            <img width="350" alt="product-mgt-mv" src="https://user-images.githubusercontent.com/69070044/230580642-468e2b7d-84d4-4163-a9bf-b1370093a8b6.png">
            <img width="350" alt="product-mgt2-mv" src="https://user-images.githubusercontent.com/69070044/230580726-cca59555-6901-46b1-8c57-d64e820d2097.png">
    - ### Future Features
        I intend to incorporate the following features in the near future:
        - Product size
        - Sales reports
        - Additional payment methods
        - Additional user account features
        - Product options
        - Ticketing Sytem
- ## Testing Phase
- ## Deployment
    - The deployed site can be visited here: <a href="https://gregmediscrubs.herokuapp.com/" target="_blank">Gregmediscrub</a>. 
    - I have included details of my initial deployment in a separate document called [DEPLOYMENT.md](./DEPLOYMENT.md).
- ## Technologies used
    - Python:
        - The packages installed for the project can be found in the [requirements.txt](./requirements.txt)
    - Django:
        - as the python framework in the project.
    - Django all auth:
        - to handle user authentication and related tasks i.e. sign in, sign up, sign out.
    - Heroku:
        - for deployment.
    - Heroku PostgreSQL & ElephantSQL:
        - for database during deployment.
    - SQLlite3:
        - used during development as a database to test models.
    - HTML:
        - the base language used to lay out the skeleton of all templates.
    - CSS:
        - to style the page and make the appearance look a little more unique.
    - Javascript:
        - to manipulate the DOM and communicate with the backend to create, read, update, and delete data from the database.
    - jQuery:
        - to simplify the use of Javascript.
    - Jinja:
        - templating language used to implement the views.py logic and models.py data into a template so it could be displayed to the user.
    - Bootstrap:
        - to style HTML, CSS.
    - Font awesome:
        - For icons.
    - AWS S3:
        - to store static and media files.
    - Stripe:
        - to handle payments.
- ## Credits
    - I am very grateful to <a href="https://www.wearfigs.com/pages/women-home" target="_blank">FIGS</a> for allowing me to use their images
- ## Media
    - All image for this project was gotten from <a href="https://www.wearfigs.com/pages/women-home" target="_blank">FIGS</a>