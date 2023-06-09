# Greg-Medi-Scrub
Gregmediscrub is a fictional hospital attire store designed and implemented with Django, Python, HTML, and CSS. It aims to provide an easy-to-use interface where customers can browse all items at once or sort into specified categories. The site offers search functionality and an inbuilt stock system to ensure users cannot buy things that are not currently in stock. Once signed in, users can save an address to their profile for easy and convenient checkout.

<img width="1404" alt="Am I responsive" src="https://user-images.githubusercontent.com/69070044/231084246-6b89e7e8-ddf6-4bc7-840c-cd9157b6da5c.png">

The deployed site can be visited here: <a href="https://gregmediscrubs.herokuapp.com/" target="_blank">Gregmediscrub</a> for more options.

# Table of Contents
- [Planning Phase](#planning-phase)
    - [Strategy](#strategy)
        - [Buiness Model](#buiness-model)
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
    - [Marketing Stratergy](#marketing-strategy)
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
        - [Orders](#orders)
        - [Inquiry](#inquiry)
        - [Review Ratings](#review-ratings)
        - [Testimonial](#testimonial)
    - [Future Features](#future-features)
- [Testing Phase](#testing-phase)
- [Deployment](#deployment)
- [Technologies used](#technologies-used)
- [Credits](#credits)
- [Media](#media)

---

## PLANNING PHASE
- ### Strategy
    - ### Buiness Model
        The following buiness model will be utilised to ensure the success of the online store.

        1. Value Proposition: Providing high-quality medical scrubs to healthcare professionals at affordable prices.

        2. Target Market: Healthcare professionals, such as doctors, nurses, and other medical staff.

        3. Revenue Model: The business generates revenue through the sale of medical scrubs, with a focus on offering competitive prices and frequent discounts to drive sales.

        4. Product Strategy: The online store offers a wide range of medical scrubs in various sizes, colors, and styles, to cater to the diverse needs of healthcare professionals. The store sources its products from reliable suppliers to ensure quality and consistency.

        5. Marketing Strategy: The business leverages digital marketing channels such as social media, email marketing, and paid advertising to reach its target market. It also partners with medical institutions and healthcare organizations to expand its reach and build brand awareness.

        6. Customer Service: The business prioritizes customer satisfaction by offering a hassle-free shopping experience, easy returns and exchanges, and responsive customer support via email, phone, and live chat.

        7. Logistics and Fulfillment: The business partners with reputable shipping carriers to ensure timely delivery of orders, while also offering free shipping for orders above a certain amount. It also implements a streamlined order fulfillment process to minimize errors and delays.

        8. Technology and Operations: The online store is built on a reliable ecommerce platform with features such as secure payment processing, inventory management, and order tracking. The business also uses data analytics to gain insights into customer behavior and optimize its operations.

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
        | Site testimonial | 5 | 3
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
        | Order Status | 2 | 3
        | Ability to edit order until status set to processing | 1 | 5
        | Store blog | 1 | 5
        | Full CRUD functionality | 5 | 5
        | Customer Inquiry | 3 | 5
        | ----- | ----- | -----
        | Total| 130 | 135

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
        Based on the above information, I have designed a flowchart using [lucid app](https://lucid.app/documents#/dashboard) to assist me in understanding how the user will move through the essential features of the online store. While minor modifications may be made to this initial user experience plan during the Agile development process, the general framework will remain consistent.
        ![PP5](https://user-images.githubusercontent.com/69070044/231914384-bccbb699-782c-4a3b-9c21-c188ee00b506.jpeg)
        - ### User Stories:
            - EPIC 1 - Product browsing Search:
                - As a shopper, I want to be able to search for products by entering keywords or by brand so that I can easily find what I am looking for
                - As a shopper, I want to be able to see high-quality product images and descriptions when I search for product so that I can make an informed purchase decision
                - As a shopper, I want to be able to sort my search by relevance, price, popularity so that I can find the product that is best for me

            - EPIC 2 - Shopping cart and Checkout:
                - As a shopper, I want to be able to easily add products to my cart so that I can keep track of the items I want to purchase
                - As a shopper, I want to be able to view the content of my cart and see the total cost of my purchase so that I can make sure I have everything I need before checkout
                - As a shopper, I want to be able to adjust the quantity of items in my cart so that I can control how many of each product I want to buy
                - As a shopper, I want to be able to remove items from my chart so that I can change my mind about a purchase
                - As a shopper, I want to be able to select a payment option so that I can pay for the items I want to purchase

            - EPIC 3 - Site Admin and Store Management:
                - As a site admin, I want to easily manage and update product information, so that I can keep my online store up-to-date
                - As site admin, I want to be able to view and manage customer orders and shipping information, so that I can keep track of my sales.

            - EPIC 4 - Product Reviews and Product detail Page:
                - As a shopper, I want to be able to view high-quality product images so that I can get a good look at the product before purchase
                - As a shopper, I want to be able to see product reviews as well as product details such as product image, description and materials so that I can make informed purchase decision.
                - As a shopper, I want to be able to add the product to my cart so that I can purchase it quickly
                - As a customer who is authenticated and purchased a product, I want to be able to review that products and give feedback.

            - EPIC 5 - User Account Management:
                - As a user, I want to be able to sign up for an account so that I can easily track my orders and save my information for future purchases.
                - As a user, I want to be able to log in to my account so that I van access my saved order history
                - As a user, I want to be able to reset my password if I forget so that I can regain access to my account
                - As a user, I want to be able to update my account information (such as name and address etc), so that my information is always up-to-date
                - As a user, I want to be able to view my order history so that I can keep track of all my purchases

            - EPIC 6 - Order Management:
                - As a shopper, I want to be able view my order history so that I can easily see what I've purchase in the past
                - As a shopper, I want to be able to manage my account information so that I can keep billing information up to date.

            - EPIC 7 - Payment Option:
                - As a shopper, I want to be able to purchase using my credit card, so that I can make transaction quickly and securely
                - As a registered shopper with an account, I want to be able to save my payment information for future purchases, so that I don't have to enter it every time I shop
                - As a security-conscious shopper, I want to be able to use a secure payment option, such as PayPal or stripe to protect my personal and financial information

            - EPIC 8 - Customer Testimonial
                - As a site visitor, I want to see the list of customers who have given testimonies about the product they bought, sso that I can make an informed purchase without spending too much time researching.
                - As a site visitor, I want to read testimonial details (including testimonial image and name) from customers who have purchased scrubs from the site, so that I can trust the quality and comfort of the scrubs before I make a purchase.
                - As the site admin, I want to be able to add testimonies that customers who have purchased a scrub have sent to me, so that potential customer can understand how good and reliable our products are
                - As the site admin, I want to be able to edit and delete testimonies if the customer wants to change details of their testimony.


            - EPIC 9 - Customer Inquiry
                - As an authenticated user with an account, I want to be able to log any questions or inquiry I have, so that there is a mean of communication between me and the site admin/site owner.
                - As the site user, I want to be able to show the site user a message box stating that their inquiry has been noted and that we will get back to them as soon as possible.
                - As the site user, I want authenticated customer to be able to send testimonies via the inquiry form if they wish to, so that I can get feedback on how we are doing as a company 

           - EPIC 10 - Marketing
                - As a business owner, I want to be able to send promotional emails so that I can promote new products and offers to my customers.
                - As a business owner, I want to be able to set up a social media page so that I can promote my business and products to the global market.
                - As a business owner, I want to be able to increase my search engine ranking so that I can increase the number of visitors to my site.


    - ### Skeleton
        - ### Wireframes
            The Balsamiq wireframing tool was utilized to create visual representations of the website's design and functionality. The wireframes utilized in the layout planning process are provided below. Nonetheless, certain alterations or eliminations were made during the development phase due to limitations of time or feasibility.
            - Home Page:
            [Wireframe for Desktop Home Page ](./docs/WireframeHomePageDesktop.jpg)
            - Products Page:
            [Wireframe for Desktop Product Page ](./docs/WireframePP.jpg)
            - Product Details Page
            [WireframeProductDetail](./docs/WireframeProductDetailDeskstop.jpg)
            - Checkout Page:
            [WireframeCheckout](./docs/WireframeCheckoutDesktop.jpg)
            - User Profile Page:
            [Wireframe Profile pageDesktop](./docs/WireframeProfilepageDesktop.jpg)
            - Testimonial List Page:
            [Wireframe Testimonial list](./docs/WireframeTestimonilalistDesttop.jpg)
            - Testimonial Detail Page:
            [Wireframe Testinonial Detail](./docs/WireframeTestinonialDetailDesktop.jpg)
            - Inquiry Page:
            [Wireframe Inquiry Page](./docs/WireframeInquiryDesktop.jpg)
        - ### Database Schema:
            - The database table scheme was created using <a href="https://drawsql.app/" target="_blank">drawsql.app</a> is explained below.
                - A Category can have multiple Products, but a Product belongs to only one Category. This is represented by a one-to-many relationship between Category and Product.
                - A Product can have multiple ReviewRatings, and each ReviewRating is associated with one Product and one User. This is represented by a many-to-one relationship between Product and ReviewRating, and a many-to-one relationship between User and ReviewRating.
                - A User can have multiple Testimonials, but each Testimonial is associated with one User. This is represented by a one-to-many relationship between User and Testimonial.
                - A User can have one UserProfile, but each UserProfile is associated with one User. This is represented by a one-to-one relationship between User and UserProfile.
                - A CustomerInquiry can have multiple InternalCommunicationNotes, but each InternalCommunicationNotes is associated with only one CustomerInquiry. This is represented by a one-to-many relationship between CustomerInquiry and InternalCommunicationNotes.
                - An Order can have multiple OrderLineItems, and each OrderLineItem is associated with one Order and one Product. This is represented by a many-to-one relationship between Order and OrderLineItem, and a many-to-one relationship between Product and OrderItem. An Order is associated with one UserProfile, but a UserProfile can be associated with multiple Orders. This is represented by a many-to-one relationship between UserProfile and Order.
                - Full ERD from PgAdmin: <a href="https://drawsql.app/teams/greg-7/diagrams/erd-gregmediscrubs" target="_blank">Database Models</a> 
                - [ERD can be found here](./docs/drawSQL-erd-gregmediscrubs-export-2023-04-07.png)
    - ### SEO considerations
        - Keywords
            - The following keywords were used for the website for optimazation; medical scrubs, scrub uniforms, nursing scrubs, medical uniforms, scrub tops, scrub pants, scrub sets, petite scrubs, tall scrubs, plus size scrubs, maternity scrubs, medical lab coats, dental scrubs, veterinary scrubs, surgical scrubs, healthcare scrubs, hospital scrubs, nursing shoes, compression socks, medical accessories
        - Page Titles
            - Each page shows an extra title after the store name to assist help with SEO.
        - Robots.txt and sitemap.xml
            - Robots.txt and sitemap files have been added to the site. This can be found in the project level directories.
    - ### Content
        Due to the nature of the site, there were limited opportunities for textual content. As many of the keywords were product-related, I focused on utilizing heading and semantic tags effectively to ensure a high-quality search rating.
    - ### Surface
        After planning the project, selecting an appropriate theme became the next step. While aiming for simplicity, I incorporated color to enhance the site's visual appeal. To maintain a clean and user-friendly design, I employed ample white space throughout.
        - Colour Scheme
            - The color scheme was kept really simple. Black and white are used to served as the primary colors on the site.
        - Typography
            - <a href="https://fonts.google.com/specimen/DM+Sans?query=dm+s" target="_blank">DM Sans</a> was utilized for the primary headings and logo, this font is clean and straightforward, ensuring legibility while also making a bold statement.

- ### Agile Development Process
    - The plan for this project was carried out using the Agile Methodology in Github. Epics and User Stories were created using [issues](https://github.com/gozygreg/gregmediscrubs/issues) on git hub. Each user story explicitly explains the purpose of the issues. Each story was assigned a classification of must-have, should-have and could-have. It was prioritised using GitHub labels with different colors. See link to kanban board [here](https://github.com/users/gozygreg/projects/15). Various tasks performed were also itemized using the agile methodology in Github.

- ### E-commerce Application Type
    - Our platform operates on a Business-to-Customer (B2C) model, enabling medical professionals to easily purchase high-quality scrubs at competitive prices from the comfort of their homes or workplaces. This website is designed to be user-friendly, with a streamlined interface that allows customers to browse and purchase products with ease. Our product catalogue features a wide range of medical scrubs in various colors and sizes, ensuring that our customers can find the perfect fit for their unique needs. To make the shopping experience more convenient, we offer secure payment options, fast shipping, and hassle-free returns. Our platform is also optimized for mobile use, enabling customers to access the site on-the-go from any device.

- ### Marketing Strategy
    - We have utilized several marketing strategies to create awareness for our scrubs. Developing a strong brand identity is crucial, which involves designing a unique logo, selecting a color scheme that aligns with the medical industry, and creating a tagline that resonates with our target audience. Our website is optimized for search engines by using relevant keywords in our content, meta tags, and URLs to ensure potential customers can easily find us on Google.

    - We have also established a Facebook business page and plan to post regularly to boost social media exposure. Targeted Facebook ads will also be utilized to reach our audience and increase engagement. We aim to collaborate with influencers in the medical industry to gain more exposure and credibility among our target audience. See link to our [facebook](https://www.facebook.com/profile.php?id=100091470390293) page.
    - In addition, we offer special promotions and discounts to both first-time customers and loyal ones to encourage them to purchase from us. Our products page has a "freebie" button that offers several promotions, and we hope this will keep our customers coming back. See image below for our promotion section on the site:
    <img width="1000" alt="freebies" src="https://user-images.githubusercontent.com/69070044/231901308-05e950d6-5908-4fcf-87e3-97c00afd014b.png">
    - Creating helpful content, such as blog posts, that educates our target audience about the benefits of wearing medical scrubs and how to properly care for them is also part of our marketing strategy. Attending trade shows and events in the medical industry to showcase our medical scrubs and network with potential customers and partners is another way we plan to promote our ecommerce business.

    - Overall, a combination of these marketing strategies can effectively promote our ecommerce business that sells medical scrubs.
- ## Features
    - ### Common to All Pages
        - ### Navbar
            - Desktop
            <img width="1000" alt="header-dv" src="https://user-images.githubusercontent.com/69070044/230581318-efc69a72-d44e-464f-b27d-69a3ec7b9ad1.png">
            - Mobile <br>
            <img width="350" alt="header-mv" src="https://user-images.githubusercontent.com/69070044/230581479-7c1f888a-4c9b-4f78-ac5d-0f091a4090a5.png"> <br>
            <img width="350" alt="nav-bar-mobile" src="https://user-images.githubusercontent.com/69070044/230593234-6a8c9d0c-468b-4bd9-beaf-74fedea20979.png">
            - Account menu
                - Unauthenticated <br>
                <img width="350" alt="account-unauthenticated" src="https://user-images.githubusercontent.com/69070044/230594669-08f62c1a-ae3a-4a5b-95d9-c9d2ec17e378.png"> 
                - Authenticated <br>
                <img width="350" alt="account-authenticated" src="https://user-images.githubusercontent.com/69070044/230594622-c786b2f1-fdae-4cdc-8ccf-6721e3ad1440.png">
                - Super User/Admin <br>
                <img width="1000" alt="account-superuser" src="https://user-images.githubusercontent.com/69070044/230593240-4c981742-36d6-4c69-97d7-dbcc331e0f48.png">
            - Bag icon <br>
            <img width="350" alt="bag-icon" src="https://user-images.githubusercontent.com/69070044/230593254-d9cb1094-c815-4ddb-8289-fe8972df879a.png">
            - Message notifications <br>
            <img width="350" alt="message notifications-mv" src="https://user-images.githubusercontent.com/69070044/230593236-1ba101a8-21cb-4963-b476-5a1e5ac54504.png">
            <img width="1000" alt="message-notification-dv" src="https://user-images.githubusercontent.com/69070044/230593239-b46e21e4-f262-4c46-b7e0-fbf586bb4588.png">


        - ### Footer
            - Desktop
            <img width="1000" alt="footer-dv" src="https://user-images.githubusercontent.com/69070044/230580535-1f75190e-8e26-41fd-b9da-8df423024abe.png">
            - Mobile <br>
            <img width="350" alt="footer-mv" src="https://user-images.githubusercontent.com/69070044/230580574-612edad8-1885-4487-a355-fd5d2e120ea4.png">
            - Common Features to both Desktop and Mobile
                - Social Media Links
                     <img width="1000" alt="Gmw facebook buisness page" src="https://user-images.githubusercontent.com/69070044/229380888-b6bef8b7-410b-4c22-856c-9b8260651f5a.png">
                - Sitemap
                <img width="1000" alt="sitemap" src="https://user-images.githubusercontent.com/69070044/230581556-281d205b-7f16-4a7c-81b7-b2b2f019c581.png">
        - ### Notifications
            <img width="350" alt="message notifications-mv" src="https://user-images.githubusercontent.com/69070044/230593236-1ba101a8-21cb-4963-b476-5a1e5ac54504.png">
            <img width="1000" alt="message-notification-dv" src="https://user-images.githubusercontent.com/69070044/230593239-b46e21e4-f262-4c46-b7e0-fbf586bb4588.png">
    - ### Page content
        - ### Home Page
            - Desktop
            <img width="1000" alt="home-page-dv" src="https://user-images.githubusercontent.com/69070044/230580158-a3709679-0626-46bf-9341-d205fc07a247.png">
            - Mobile <br>
            <img width="350" alt="home-page-mv" src="https://user-images.githubusercontent.com/69070044/230580185-d7d480eb-e457-4504-aeb6-0d81136ea137.png">
        - ### Products Page
            - Desktop
            <img width="1000" alt="product-page-dv" src="https://user-images.githubusercontent.com/69070044/230580465-4369af91-7566-4fef-bcb2-d299c297e4db.png">
            - Mobile <br>
            <img width="350" alt="product-page-mv" src="https://user-images.githubusercontent.com/69070044/230580495-cec54dcd-38e5-4143-b95b-ece44d2efc25.png">
        - ### Product Details Page
            - Mobile <br>
            <img width="350" alt="product-detail-mv" src="https://user-images.githubusercontent.com/69070044/230593253-f3efcba2-6483-41cb-80f9-4205ff0966d7.png">
        - ### Reviews
            Only authenticated users that have purchased a product can review the product.
            - Desktop
            <img width="1000" alt="reviews-section-dv" src="https://user-images.githubusercontent.com/69070044/230580773-d0b1826e-9447-45c0-9e92-2147356379a0.png">
            - Mobile <br>
            <img width="350" alt="reviews-section-mv" src="https://user-images.githubusercontent.com/69070044/230580810-78882c5a-68af-479d-a8b8-47b6563cf0a9.png">
        - ### Edit product - frontend form
            Only site admin have access to edit or delete a product. Below is the product edit from
            <img width="1000" alt="product-edit-page" src="https://user-images.githubusercontent.com/69070044/230597856-d189e0ad-a49f-4db6-b237-380c543b55b5.png">
        - ### Bag
            - Desktop
            <img width="1000" alt="bag-page-dv" src="https://user-images.githubusercontent.com/69070044/230580233-93f2f331-358b-4aae-9dec-aabe088cbe40.png">
            - Mobile <br>
            <img width="350" alt="bag-page-mv" src="https://user-images.githubusercontent.com/69070044/230580251-fae07268-7995-498c-a277-f32e77a5a02b.png">
        - ### Checkout
            - Desktop
            <img width="1000" alt="checkout-dv" src="https://user-images.githubusercontent.com/69070044/230593246-09f3b193-0695-49ea-80b3-cb13ab21501e.png">
            - Mobile <br>
            <img width="350" alt="checkout-mv" src="https://user-images.githubusercontent.com/69070044/230593244-a652c26c-b96d-4077-b3cc-c5dd15d55467.png">
        - ### Checkout Success
            - Desktop
            <img width="1000" alt="checkout-success-dv" src="https://user-images.githubusercontent.com/69070044/230593250-8e24d952-7315-4551-a884-018c95293814.png">
            - Mobile <br>
            <img width="350" alt="checkout-success-mv" src="https://user-images.githubusercontent.com/69070044/230593247-ab684c44-1d0e-48b3-80bc-fd5358567a9d.png">
        - ### Testimonial
            - ## Testimonial list
                - Desktop
                <img width="1000" alt="testimonial-list-dv" src="https://user-images.githubusercontent.com/69070044/230580860-a6deee2a-03f7-43b5-9bf2-b99997a45a8d.png">
                - Mobile <br>
                <img width="350" alt="testimonial-list-mv" src="https://user-images.githubusercontent.com/69070044/230580896-44763bda-f845-420e-8c4c-a66adfd5febc.png">
            - ## Testimonial detail
                - Desktop
                <img width="1000" alt="testimonial-detail-dv" src="https://user-images.githubusercontent.com/69070044/230580942-8ed898a1-539b-47d6-8f21-4301defb3e03.png">
                - Mobile <br>
                <img width="350" alt="testimonial-detail-mv" src="https://user-images.githubusercontent.com/69070044/230580971-69089bb0-eb2d-4087-a803-249b0a7b259b.png">
        - ### Profile
            - Desktop
            <img width="1000" alt="profile-page-dv" src="https://user-images.githubusercontent.com/69070044/230580048-7505a087-8d55-44a0-9286-3d45779e838b.png">
            - Mobile <br>
            <img width="350" alt="profile-page-mv" src="https://user-images.githubusercontent.com/69070044/230580091-a6851079-52d6-4a73-8465-be987fbf4939.png">
        - ### Inquiry
            - Desktop
            <img width="1000" alt="inquiry-page-dv" src="https://user-images.githubusercontent.com/69070044/230580397-35194ef1-21fa-46aa-bef9-418c1efa3ebe.png">
            - Mobile <br>
            <img width="350" alt="inquiry-page-mv" src="https://user-images.githubusercontent.com/69070044/230580418-b4d011e0-8e13-48d9-af30-42c15a6e3ae1.png">
        - ### Authentication
            - Django all-auth library was used to handle authentication on the site. The functionality includes; loging in/out, sign up/register, reset password, verifying email and email confirmation.
            - Signup
                    - Desktop
                    <img width="1000" alt="signup-dv" src="https://user-images.githubusercontent.com/69070044/230595988-eeb0a1d1-0f50-4e42-8e4d-b581059c34bd.png">
                    - Mobile <br>
                    <img width="350" alt="signup-mv" src="https://user-images.githubusercontent.com/69070044/230595985-c340987f-4bff-4b63-b952-0860672f72e7.png">
                - Sign In
                    - Desktop
                    <img width="1000" alt="signin-dv" src="https://user-images.githubusercontent.com/69070044/230595989-6f02134e-6402-40a4-a66f-371e4508a669.png">
                    - Mobile <br>
                    <img width="350" alt="signin-mv" src="https://user-images.githubusercontent.com/69070044/230595991-ae5e5084-4e4f-47f8-bf6f-133291629109.png">
                - Sign Out
                    - Desktop
                    <img width="1000" alt="signout-page-dv" src="https://user-images.githubusercontent.com/69070044/230580308-1c6f236e-20d3-47e6-ba9e-1c4421b4087e.png">
                    - Mobile <br>
                    <img width="350" alt="signout-page-mv" src="https://user-images.githubusercontent.com/69070044/230580351-018b70a7-6f0f-4386-86e8-5b9b21aaf4fb.png">
        - ### 404 Page
            <img width="1000" alt="404" src="https://user-images.githubusercontent.com/69070044/230581541-d4885d67-6888-4627-85f8-664c95ae0316.png">
        - ### Responsive Design
            All pages are fully responsive. I tested the responsiveness on chrome dev tool and on the following devices (This is not an exaustive list);
            - Iphone SE
            - Iphone XR
            - Iphone 12 pro
            - Pixel 5
            - Samsung galaxy S8 +
            - Ipad Air
            - Ipad Mini
            - Media query was used to also control responsiveness to various screen sizes:
                - @media (min-width: 1200px)
                - @media (min-width: 992px) 
                - @media (max-width: 991px) 
                - @media (min-width: 770px) and (max-width: 1380px)
                - @media only screen and (max-width: 768px)
            - [Am I responsive](https://ui.dev/amiresponsive) was also utilised check the responsiveness of my site

- ## Admin Panel for Store Admin
    - ### Admin Panel Overview
        - ### Products
            Super user is able to add, edit and delete product via the frontend as well as the back end.
            - Desktop
            <img width="1000" alt="product-mgt-dv" src="https://user-images.githubusercontent.com/69070044/230580619-762247d4-b930-4c57-97af-83dcec9094c8.png">
            <img width="1000" alt="product-mgt2-dv" src="https://user-images.githubusercontent.com/69070044/230580693-601cff94-cd39-476d-9e51-660a987c6cee.png">
            - Mobile <br>
            <img width="350" alt="product-mgt-mv" src="https://user-images.githubusercontent.com/69070044/230580642-468e2b7d-84d4-4163-a9bf-b1370093a8b6.png"> <br>
            <img width="350" alt="product-mgt2-mv" src="https://user-images.githubusercontent.com/69070044/230580726-cca59555-6901-46b1-8c57-d64e820d2097.png">
        - ### Inquiry
            Within the admin panel, the superuser has access to view any messages received through the "contact us" form, as well as a section for leaving internal notes for other staff members. In the future, a ticketing system will be implemented, allowing the admin to reply and make it visible to the customer on the front end. Despite this, the current system allows the customer to leave a message and for the admin to leave notes regarding necessary actions or responses sent by email. To assist staff members in tracking replied messages, a feature has been enabled to mark messages as replied to, defaulting to a pending reply status. Additionally, various filter options are available for staff to sort by status and date.
            Customers who do not have any inquiries but want to send a testimonial can do so by using the inquiry form. There will be a future upgrade where a separate form will be build to handle customer testimonial.
        - ### Orders
            Also, within the admin panel, superuser is able to see the various orders customers has placed.
        - ### Review Ratings
            Through the administrative panel, the superuser has the ability to perform CRUD operations such as adding, deleting, or modifying reviews. In addition, customer reviews can be accessed by customer via the frontend. It should be noted that customers can only add product reviews if they meet two conditions: they must be registered users and have purchased the product.
        - ### Testimonial
            The superuser has the authority to include testimonials from customers who have purchased products from our company in the past and are happy with the overall service we rendered. Unlike review ratings that concentrate on assessing a specific product, customer testimonials revolve around the overall experience of dealing with our company. The superuser has the power to perform CRUD operations on these testimonials. Nonetheless, customers have the option of sharing their testimonials by utilizing the inquiry field or by sending an email to us.
    - ### Future Features
        There is a lot of potential in this project and although there is a viable MVP, there are many additional features I would like implement in the future:
        - Product size
        - Sales reports
        - Additional payment methods and international payments (Currency converter)
        - Stock management and Track order functionalities
        - Ticketing Sytem
        - Allow customer to add testimonial from the front end
- ## Testing Phase
I have included testing details during and post-development in a separate document called [TESTING.md](./TESTING.md)
- ## Deployment
    - The deployed site can be visited here: <a href="https://gregmediscrubs.herokuapp.com/" target="_blank">Gregmediscrub</a>. 
    - I have included details of my initial deployment in a separate document called [DEPLOYMENT.md](./DEPLOYMENT.md).
- ## Technologies used
    - Python:
        - The packages installed for the project can be found in the [requirements.txt](./requirements.txt)
    - Django:
        - as the python framework in the project.
    - Django allauth:
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
    - Big shoutout to Code Institute; for the course materials, all the tutors who helped me when I was stuck. I cannot thank you guys enough!
    - Rohit Sharma - Mentor and guide. Thank you so much.
    - I am very grateful to <a href="https://www.wearfigs.com/pages/women-home" target="_blank">FIGS</a> for allowing me to use their images
    - The code institute Slack community for always being available to answer my questions.
    - [W3school](https://www.w3schools.com/)
    - [drawsql](https://drawsql.app/) was used to create the database diagram.
    - [Stackoverflow](https://stackoverflow.com/)
    - [Am I responsive](https://ui.dev/amiresponsive) website for helping me check the responsiveness of my site
    - Arno Pretorius for your youtube video on building an e-commerse store. I got load of idea from them

- ## Media
    - All image for this project was gotten from <a href="https://www.wearfigs.com/pages/women-home" target="_blank">FIGS</a>

- [back to top](#table-of-contents)