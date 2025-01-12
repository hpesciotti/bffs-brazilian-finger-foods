# BFFs | Brazilian Finger Foods

![BFFs](documentation/showcase/am_i_responsive.png)

[Visit my website here](https://bffs-brazilian-finger-foods-99657e2a95f1.herokuapp.com/)


BFFs is an online store specializing in frozen Brazilian appetizers, focusing on delivering quality snacks in an easy and intuitive manner. The e-commerce platform is accessible through all browsers and fully responsive across different screen sizes.

### Features for Users
Through the web application, users can:

- Browse the store as guests.
- Register for an account.
- Explore products by category and price.
- View, add, and edit products in their shopping bag.
- As registered users, access their order history.
- Sign up for promotional newsletters.

### Features for the Store Owner
The store owner can:

- Manage products, quickly toggle best-seller status (visible on the home page) and edit prices.
- Manage batches with full CRUD functionality, allowing them to:
  - Create discounts.
  - Edit existing batches.
  - Delete batches.

### Feel free to Test my Web Application
For purchase you can use the following [Stripe Dummy Card](https://stripe.com/docs/testing) details:

- Card Number: 4242424242424242
- 3D Secure Auth Number: 4000 0027 6000 3184
- Exp Date: Any date in the future using the format MM/YY
- CVN: any 3 digit number
- Postcode (Card): any 5 numerals  

For Django Admin access with relevant sign-in credentials use this link: [BFFs Django Admin](https://bffs-brazilian-finger-foods-99657e2a95f1.herokuapp.com/admin/)

For access to Shop Admin panel in the frontend view with relevant sign-in credentials use: [BFFS Shop Admin](https://bffs-brazilian-finger-foods-99657e2a95f1.herokuapp.com/shop_admin/)


## Readme - Table of Contents

1. [Introduction](#1-introduction)

2. [UX Design](#2-ux-design)

    2.1. [Strategy/Scope and Structural Plane](#21-strategyscope-and-structural-plane)

    2.2. [User Stories](#22-user-stories)
    
    2.3. [Skeleton & Surface Planes](#23-skeleton--surface-planes)

    2.4. [Design](#24-design)

    2.5. [Agile and Project Managing](#25-agile-and-project-managing)

3. [Features](#3-features)

    3.1. [User View](#31-user-view)

    3.2. [CRUD Functionality](#32-crud-functionality)

    3.3. [Future Features](#33-features-showcase)

    3.4. [Future Features](#34-future-features)

4. [Technologies Used](#4-technologies-used)  

    4.1. [Languages Used](#41-languages-used)

    4.2. [Frameworks, Libraries & Programs Used](#42---frameworks-libraries-technologies--programs-used)

5. [Testing](#5-testing)

6. [Deployment](#6-deployment)

    6.1. [Code Institute PostgreSQL Database](#61-code-institute-postgresql-database)

    6.2. [Connecting to GitHub](#62-connecting-to-github)

    6.3. [Django Project Setup](#63-django-project-setup) 

    6.4. [Cloudinary API](#64-cloudinary-api)

    6.5. [Heroku Deployment](#65-heroku-deployment)

    6.6. [Clone Project](#66-make-a-local-clone-project)

    6.7. [Clone Project](#67-clone-project)

7. [Credits](#7-credits)

   7.1. [Content](#71-content)

   7.2. [Media](#72-media)

   7.3. [Acknowlegements](#73-acknowlegements)


## **1. Introduction**

BFF would consist of a small business specializing in Brazilian appetizers in Dublin. The growing Brazilian community and the cosmopolitan nature of the Irish capital—where cuisines from all over the world are represented—make this business venture promising.

An acronym for Brazilian Finger Foods, BFFs is also a play on the phrase Best Friends Forever, bringing originality to the brand name. The dual meaning evokes an affectionate relationship with the comfort foods sold on the site. Acronyms are generally easier to remember, aiding in brand marketing.

Like many small businesses, given the current real estate crisis, BFF focuses on selling its products online, avoiding needing a fixed store or headquarters. This approach aims to boost sales and strengthen the brand through an attractive e-commerce platform. The sale of frozen products in the food industry offers a significant advantage: their relative longevity, with a shelf life of up to a year. This allows for better planning. The web application on the shop owner’s side includes tools for managing sales and offering discounts on products that have been in stock longer.

As an e-commerce platform, BFFs a is a fully functional e-commerce solution, combining frontend and backend tools to provide an intuitive, simple, and efficient shopping experience. It also automates billing, order processing, and stock management.

[Back to top](#readme---table-of-contents)

## **2. UX Design**

### **2.1. Strategy/Scope and Structural Plane**

Overall, the primary objective of this project was to develop an e-commerce store that met the assessment criteria of the Code Institute's Project 5: E-Commerce Module, using the Django framework. The platform was required to function as a responsive online store, integrating Stripe as the payment system, providing user and guest views for authentication (via Django Allauth), and incorporating store features alongside a demonstration of marketing and SEO skills.

I have some experience in the catering industry, where stock control was one of my responsibilities as a catering assistant. Drawing from this experience, I implemented a few ideas in the Shop Admin section within the limited time available to develop the platform. Additionally, during the creation of user stories, having completed the mock project Boutique Ado—which successfully covers most customer/user experiences—I found it interesting to add some additional nuance to the shop owner functionalities. Unfortunately, I was unable to implement all the planned features, opting to exclude some "could-have" stories (as per the MoSCoW prioritisation method) from the MVP.

From the client’s perspective, it was important to feature engaging text, appealing images, and a design that would entice users to “crave” the products. Through benchmarking several Brazilian brands, I identified the key elements they use to promote similar products and incorporated them into the website. Furthermore, a primary UX goal for the web application was to convey trustworthiness, ensuring that end users would feel confident and safe when making a purchase.

[Back to top](#readme---table-of-contents)

### **2.2. User Stories**

User Stories management was conducted in accordance with Agile planning methodologies to ensure project completion. Through [GitHub Projects](https://github.com/users/hpesciotti/projects/5), user stories were created as issues and organized into boards. Groups of user stories were assigned to a Sprint and their respective milestones. The use of labels helped to define epics and their associated tasks.

Furthermore, the user stories were categorized according to the **MoSCoW Prioritization Method** as follows:
- **Must Haves**: Essential for the MVP (Minimum Viable Product).
- **Should Haves**: Important but not critical for the MVP.
- **Could Haves**: Nice to have if time allows it.
- **Won’t Haves**: Initially brainstormed but, abandoned due to time limitations.

It is important to point out that time was a significant limiting factor, and bugs considerably delayed the project, ultimately resulting in a scope change. As a result, all **Could Have** features and User Stories are not currently implemented and have been set as **Future Features**.

The complete list of User Stories is available at [GitHub Projects](https://github.com/users/hpesciotti/projects/5).

[Back to top](#readme---table-of-contents)

#### User Story #1 - Epic: Home - Must Have

As a **Customer**, I want to be able to **navigate the site's home page** so that I can **familiarize myself with the type of products and services offered, identify clearance items and special offers.**

##### Acceptance Criteria  
- **AC 1:** The home page displays a straightforward navigation menu with links to product categories, special offers, and the clearance section.  
- **AC 2:** A search bar is available and functional for quick access to the various links and categories of the products.  
- **AC 3:** A carousel container with appealing images of finger foods, summarized descriptions, and persuasive call-to-action phrases encouraging product purchases.  
- **AC 4:** A card-carousel container displaying featured products, clearance, and most sold items.

### User Story #2  - Epic: All Products/Home - Must Have

As a **Customer**, I want to be able to **view deals, clearance products, and special offers** so that I can **take advantage of special prices on products.**

#### Acceptance Criteria  
- **AC 1:** The product pages consist of sections pre-filtered by main categories in the navigation bar or a category menu.  
- **AC 2:** Clicking on a category filters the product database list to display only the selected type.  


### User Story #3  - Epic: All Products/Home - Must Have

As a **Customer**, I want to be able to **browse the products advertised** so that I can **get general information, such as product image, price, allergens, and ingredients.**

#### Acceptance Criteria  
- **AC 1:** Product pages, listed by categories, feature products displayed in a grid or list format with images, names, and prices.  
- **AC 2:** Clicking on a product redirects the user to a detailed product page.  


### User Story #4 - Epic: All Products - Must Have

As a **Customer**, I want to be able to **effortlessly find products that cater to a dietary preference or condition** so that I can **sort the available products to filter the desired appetizer (gluten-free, dairy-free, vegan) or regarding the cooking process (fried/baked) or assorted bundles.**

#### Acceptance Criteria  
- **AC 1:** A filter menu is available on the product listing page with options for:  
  - Gluten-free  
  - Dairy-free  
  - Vegan  
  - Fried  
  - Baked  
  - Assorted Bundles  
- **AC 2:** A sorting feature includes options for prices.  
- **AC 3:** Selected filters dynamically update the displayed products.  


### User Story #5 - Epic: All Products - Must Have

As a **Customer**, I want to be able to **view a product page with general information of a selected appetizer** so that I can **see ingredients, dietary information, history, and the region of Brazil.**

#### Acceptance Criteria  
- **AC 1:** The product page includes:  
  - Full-size product image  
  - Ingredients list  
  - Dietary information table  
  - Product description, including history and origin in Brazil  
- **AC 2:** The information should be presented in a responsive layout like an accordion.  


### User Story #6 - Epic: FAQ - Should Have

As a **Customer**, I want to be able to **know about storage, cooking information, and general frequently asked questions** so that I can **read about any possible doubts regarding the offered products.**

#### Acceptance Criteria  
- **AC 1:** The About page includes the following:  
  - Storage instructions  
  - Cooking or preparation guidelines  
  - A FAQ section  
- **AC 2:** The FAQ section answers common questions like shelf life, freezing compatibility, and preparation methods.  
- **AC 3:** The information is easy to navigate and clear for comprehension.


### User Story #7 - Epic: Customer Profile Page - Must Have

As a **Customer**, I want to be able to **easily create/register a user account** so that I can **manage key user information, such as address and personal details.**

#### Acceptance Criteria  
- **AC 1:** The registration page is accessible from the home page via a "Sign Up" button.  
- **AC 2:** Error messages are displayed for invalid inputs.  
- **AC 3:** Registration is handled by Django Allauth. 


### User Story #8 - Epic: Customer Profile Page - Must Have

As a **Customer**, I want to be able to **manage my account through a user profile** so that I can **manage my order history and personal information.**

#### Acceptance Criteria  
- **AC 1:** Users can access their profile via a "My Account" link in the navigation bar.  
- **AC 2:** The user profile page includes sections for:  
  - Personal details (e.g., name, email)  
  - Address details  
  - Order history (sortable by date and status)  
- **AC 3:** Users can update their information and save changes.

### User Story #9  - Epic: Customer Profile Page - Must Have

As a **Customer**, I want to be able to **effortlessly log in/ logout of my account** so that I can **efficiently access my account**

#### Acceptance Criteria  
- **AC 1:** The login page is accessible from the home page via a "Log In" button.  
- **AC 2:** Users can log in using their registered email and password.  
- **AC 3:** A "Log Out" button is always visible when the user is logged in.  
- **AC 4:** Error messages are displayed for invalid login attempts (e.g., incorrect email or password).  


### User Story #10 - Epic: All Products Pages / Checkout - Must Have

As a **Customer**, I want to be able to **easily select the quantity of products** so that I can **ensure I am purchasing the right quantity before checkout.**

#### Acceptance Criteria  
- **AC 1:** Each product page includes a quantity selector (e.g., dropdown or input field with "+" and "-" buttons).  
- **AC 2:** The quantity selector defaults to 1 but allows users to increase or decrease the quantity.  
- **AC 3:** If the quantity exceeds the available stock, an error message or alert is displayed.  


### User Story #11 - Epic: Checkout - Must Have

As a **Customer**, I want to be able to **manage my shopping bag** so that I can **check if the products selected are being added and monitor my spending.**

#### Acceptance Criteria  
- **AC 1:** The shopping bag is accessible via a cart icon in the navigation bar.  
- **AC 2:** The shopping bag displays the list of added products (names and selected quantities).  
- **AC 3:** The subtotal, taxes, and grand total are calculated and displayed.


### User Story #12 - Epic: Checkout - Should Have

As a **Customer**, I want to be able to **view notifications indicating addition, reduction and removal of items in my shopping bag** so that I can **know immediately if my actions are reflected on my shopping bag**

#### Acceptance Criteria  
- **AC 1:** A toast notification appears after any action (e.g., item added, quantity updated, item removed).
- **AC 2:** Notifications are visible for a few seconds before fading automatically.


### User Story #13 - Epic: Checkout - Should Have

As a **Customer**, I want to be able to **check out safely, entering my payment information** so that I can **be certain my personal and payment data are secure.**

#### Acceptance Criteria  
- **AC 1:** The checkout page requires users to be logged in.
- **AC 2:** Payment data is encrypted and processed securely.
- **AC 3:** An order summary (products, prices, and totals) is displayed before payment submission. 
- **AC 4:** Errors in payment details prompt a clear error message.


### User Story #14 - Epic: Checkout - Must Have

As a **Customer**, I want to be able to**visualise an order confirmation after checkout** so that I can **verify the order details and be certain that all steps of purchase were concluded with success**

#### Acceptance Criteria  
- **AC 1:** The checkout page includes fields for shipping and billing details.  
- **AC 2:** Fields include validation for required inputs (e.g., address, city, zip code).  
- **AC 3:** Payment is processed securely via Stripe integration.


### User Story #15 - Epic: Checkout - Must Have

As a **Customer**, I want to be able to **receive an email with the confirmation of my order** so that I can **be reassured that my order was confirmed.

#### Acceptance Criteria  
- **AC 1:** Upon successful payment, the system sends a confirmation email with order details.  
- **AC 2:** The email includes the order number, list of items, total amount, and delivery information.


#### User Story #16 - Epic: All Products / Customer Profile - Could Have - Future Feature

As a **Customer**, I want to be able to **read reviews of appetizers posted by other customers** so that I can **make informed purchasing decisions**.

##### Acceptance Criteria
- **AC 1:**Each product page includes a section displaying customer reviews.
- **AC 2:**Reviews include the customer’s name and comment.


### User Story #17 - Epic: All Products / Customer Profile - Could Have - Future Feature

As a **Customer**, I want to be able to **read reviews of appetizers posted by other customers** so that I can **make informed purchasing decisions.**

#### Acceptance Criteria  
- **AC 1:** Each product page includes a section displaying customer reviews.  
- **AC 2:** Reviews include the customer’s name, rating, and comment.  
- **AC 3:** Reviews are sorted by date, with the most recent appearing first.  


### User Story #18 - Epic: Admin Panel - Should Have

As a **Store Owner**, I want to be able to** Add a new product (finger food or appetizer)** so that I can **use the website to present the customers with a new product**

#### Acceptance Criteria  
- **AC 1:** The admin panel has a dedicated section for adding new products.
- **AC 2:** The product creation form includes fields from the product model.
- **AC 3:** Validation ensures all required fields are completed before submission.


### User Story #19 - Epic: Admin Panel - Should Have

As a **Store Owner**, I want to be able to **Add a new batch of an existing product** so that I can **keep records of expiry dates and quantities and maintain picture and general information of an existing product**

#### Acceptance Criteria  
- **AC 1:** The admin panel allows batch management for existing products
- **AC 2:** Store owners can add a new batch by selecting an existing product.
- **AC 3:** The batch creation form includes fields for the batch number and expiry date.
- **AC 4:** **Changed** Expired batches are flagged and excluded from active stock.


### User Story #20 - Epic: Admin Panel - Could Have - Future Feature

As a **Store Owner**, I want to be able to **Use the expiry dates or quantities to create special offers** so that I can **maintain stock control and reduce food waste and financial loss. **

#### Acceptance Criteria  
- **AC 1:** The admin panel includes a feature to create special offers for specific products, considering approaching expiry dates and overstocked products.  
- **AC 2:** Notifications alerting the store owner to create offers for products nearing expiry.
- **AC 3:** Discounted products are highlighted on the customer-facing product page with labels (e.g., "Clearance" or "Special Offer").


### User Story #21 - Epic: Admin Panel - Could Have - Future Feature

As a **Site Admin**, I want to be able to **view and manage customer orders** so that I can **track sales and ensure timely delivery.**

#### Acceptance Criteria  
- **AC 1:** Admins can view a list of all customer orders in the admin panel.  
- **AC 2:** Each order includes details like customer name, items, total, and status.  
- **AC 3:** Admins can update the order status (e.g., "Processing," "Shipped," "Delivered").  

### User Story #22 - Epic: Admin Panel - Could Have - Future Feature

As a **Store Owner**, I want to be able to**A monthly/weekly inventory of the sales sorted by products ** so that I can **plan the production of new batches or increment or decrease the batches of a particular product.**

#### Acceptance Criteria  
- **AC 1:** The admin panel provides an inventory report accessible by date range (weekly/monthly). 
- **AC 2:** The reports include:
                      - Product name.
                      - Total units sold.
                      - Revenue per product.


#### User Story #23 - Epic: Checkout - Should Have

As a **Store Owner**, I want to be able to **Have a policy page with terms and conditions** so that I can **present to the customer the general legal terms of online shopping.**

##### Acceptance Criteria
- **AC 1:** A policy page is accessible from the website footer with a link labelled "Terms and Conditions."
- **AC 2:** A checkbox confirming customer acceptance of terms is included at checkout.


#### User Story #24 - Epic: Checkout - Could Have - Future Feature

As a **Customer**, I want to be able to **apply discount codes during checkout** so that **I can redeem special offers and save money**.

##### Acceptance Criteria
- **AC 1:** The checkout page includes a field for entering discount codes.
- **AC 2:** Valid discount codes reduce the total amount.
- **AC 3:** An error message is displayed for invalid or expired codes.


#### User Story #25 - Epic: Marketing - Must Have

As a **Store Owner**, I want to be able to **have a social media presence** so that I can **promote BFFs products on social media**.

##### Acceptance Criteria
- **AC 1:** Make the brand know through Facebook Business and other relevant Social Media.
- **AC 2:** Create an newsletter.

[Back to top](#readme---table-of-contents)

### **2.3. Skeleton & Surface Planes**

#### Wireframes

The wireframes were created using **Balsamiq**. At this stage, alongside the user stories, it was possible to identify the functionalities, pages, and data to be presented in later phases.

Although the design is simple, comparing the final result with the wireframes demonstrates that the production phase successfully implemented what was proposed at the outset.

<details>
<summary>Home Desktop/Mobile</summary>

![Home Desktop](documentation/wireframes/index.png)

</details>


<details>
<summary>Products Page Desktop/Mobile</summary>

![About Mobile](documentation/wireframes/products.png)

</details>

<details>
<summary>Admin Panel</summary>

![About Mobile](documentation/wireframes/admin_panel.png)

</details>

[Back to top](#readme---table-of-contents)

#### Datbase Schema

### Data Model of the Web Application "BFFs"

The data model of the web application **BFFs**, as shown in the following diagram, is centered around the **Batch** model, which serves as the link between **Product** and **Order**. The connection between these three databases ensures the main flow of the e-commerce platform, which is as follows: a **Product** is chosen (with attributes such as images, price, names – both short widget and full), and its quantity and sale price are managed by the **Batch** model. The information, stored in a session dictionary called **bag**, is then passed to the **Order** model. The **Order** model establishes a simplified connection with the **Stripe API**, generating the order and processing the payment.

It is important to note that after the connection is established between the **Order** and **Stripe**, and the confirmation email is sent, the temporary **bag** instance is used to decrement the quantity of the product in the **Batch** database.

It is emphasized that in the case of **BFFs**, the **Product** model does not represent an actual product but rather a category or even a product typology that only passes immutable data to the frontend. The connection between **Batch** and **Product** is achieved via a **ForeignKey**, allowing multiple **Batch** elements to reference the same **Product**. This connection was chosen due to the perishable nature of the products, where multiple production batches might be available to the buyer.

The **Product** model is also linked to **DietaryCategories** through a **many-to-many** relationship. This occurs because a vegan product might also be gluten-free, dairy-free, or ovo-lacto-vegetarian. This relationship enables consumers to find products that fit their dietary preferences. This connection facilitates the categorization displayed in the site's navigation menu and allows direct searches by dietary categories via the **Search Bar** (q).

User validation is handled by **Django AllAuth**, which connects to the **UserProfile** model and allows for the recording of personal and delivery information. During checkout, this information can be saved by passing data between **Order**, **Stripe Webhook**, and **UserProfile**.

Finally, the **Faq** model manages the data displayed on the **FAQs** page. Using a **for loop**, the questions and answers are passed to the frontend and presented to the user through an accordion. This database does not connect with any other databases in the web application.

![BFFs - Data Schema](documentation/showcase/bffs.drawio.png)

[Back to top](#readme---table-of-contents)

### **2.4. Design** 

The colour scheme plays an important role in evoking a "food craving feel." The choice of main colours was inspired by some prominent Brazilian traditional food brands, such as:

- [Boca do Forno](http://bocadoforno.com.br/)
- [Swift](https://www.swift.com.br/) – A significant source of inspiration for UX, as it is very well-structured.
- [Sodiê Doces](https://sodiedoces.com.br/)
- [Fujiyama](https://fujiyamapastelaria.com/)




[Back to top](#readme---table-of-contents)

#### Colour Scheme

The colour scheme plays an important role in evoking a "food craving feel." The choice of main colours was inspired by some prominent Brazilian traditional food brands, such as:

- [Boca do Forno](http://bocadoforno.com.br/)
- [Swift](https://www.swift.com.br/) – A significant source of inspiration for UX, as it is very well-structured.
- [Sodiê Doces](https://sodiedoces.com.br/)
- [Fujiyama](https://fujiyamapastelaria.com/)



![Colour Palette](documentation/color_palette.png)

<details>
<summary>Colour Text</summary>

![Colour Text](documentation/color_text_contrast.png)

</details>

[Back to top](#readme---table-of-contents)

#### Font

I chose Josefin Sans for the items in the nav-bar and Inter Sans for the rest of the text.

### **2.5. Agile and Project Managing** 

I tried to implement Agile Methodology during the planning of my full stack framework project. The planning was conducted with [GitHub Project](https://github.com/users/hpesciotti/projects/3). I chose to limit my entries to Tasks, User Stories, linking them through GitHub interface. 

I had initially around 30 days to execute the project, as suggest by the CI Scheduler. I would like to point out that was a very short time frame to develop a full-stack application and taking into account my learning curve with Django and Boostrap, I think the endproduct can achive the MVP status. 

Here is a draft of my initial planning divided um four sprints, tackling the various content involved on Speleometrics.

| Sprint | Start       | Finish      | Content                                    |
|--------|-------------|-------------|--------------------------------------------|
| 1      | 15/09/2024  | 21/09/2024  | Design, Wireframes, Sign-In (Django AllAuth) |
| 2      | 22/09/2024  | 28/09/2024  | Defining the models, Profiles and Caves    |
| 3      | 29/09/2024  | 05/10/2024  | Statistics, Reports, Maps and Frontend Development |
| 4      | 06/10/2024  | 13/10/2024  | Styling/Testing/Documentation               |

[Back to top](#readme---table-of-contents)

### **3. Features**

#### **3.1. User view**

To ensure an engaging interface and data protection, it was necessary to establish some permissions for the website users.
Moreover, the classification of users reflects upon the user's access to some pages. 
The following charts show the accessibility of the features per user type.

| Feature / User Type       | Unlogged User | Logged User | Superuser |
|---------------------------|---------------|-------------|-----------|
| **Home**                  | Visible       | Visible     | Visible   |
| **About**                 | Visible       | Visible     | Visible   |
| **Caves**                 |               |             |           |
| - Map Search              | Visible       | Visible     | Visible   |
| - Table Search            | Visible       | Visible     | Visible   |
| - Cave Page               | Visible       | Visible     | Visible   |
| - Report Cave             | Not Visible    | Visible     | Visible   |
| **User Area**             |               |             |           |
| - Register a Cave         | Not Visible    | Visible     | Visible   |
| - My Caves                | Not Visible    | Visible     | Visible   |
| - Edit Cave               | Not Visible    | Visible     | Visible   |
| - Edit Profile            | Not Visible    | Visible     | Visible   |
| **Reports**               |               |             |           |
| - Report List             | Not Visible    | Not Visible  | Visible   |
| - Report Page             | Not Visible    | Not Visible  | Visible   |

[Back to top](#readme---table-of-contents)

#### **3.2. CRUD Functionality**

The Create, Read, Update, Delete (CRUD) functionalities are planned for Speleometrics. Through the Database Model, it is clear that full CRUD functionality is available for the Cave database, meaning that any user who has registered a cave and a superuser has access to Create, Read, Update, and Delete operations. Regarding user profiles, the only operation currently unavailable is the ability to delete them. Since cave records are crucial to the web application's purpose, deleting profiles could result in data loss (cascade effect). Therefore, the option to delete a profile was not initially planned. Additionally, as transparency is a guiding principle of the project, most functionalities are available in Read mode, even for users who are not logged in. The following chart displays the CRUD functions per page per user.

| Feature / User Type       | Unlogged User | Logged User           | Superuser         |
|---------------------------|---------------|-----------------------|--------------------|
| **Home**                  | R             | R                     | R                  |
| **About**                 | R             | R                     | R                  |
| **Cave**                  |               |                       |                    |
| - Table Search            | R             | R                     | R                  |
| - Cave Page               | R             | All = R - If owner = U, D | R, U, D          |
| - Report Cave             | R             | C                     | C                  |
| **User Area**             |               |                       |                    |
| - Register a Cave         | R             | C                     | C                  |
| - My Caves                | R             | U, D                  | R, U, D            |
| - Edit Cave               | R             | If owner = U else -  | U                  |
| - Edit Profile            | R             | All = R / If owner = U | All = R / If owner = U |
| **Reports**               |               |                       |                    |
| - Report List             | -             | -                     | R, D               |
| - Report Page             | -             | -                     | R, D               |

[Back to top](#readme---table-of-contents)

### **3.3. Features Showcase**

#### Header

The header features two versions tailored for both mobile and desktop views. Both versions include the site's logo, which has hover and focus functions aligned with the adopted colour scheme. The logo follows current trends by maintaining a minimalist design.

In the desktop version, links are presented as nav-pills, responsive to hover, focus, and active states. The purpose of the nav-pills is to effectively indicate the section or area of the site being accessed. It is important to note that the "add cave" section, which depends on user validation and is accessed through the user area, sits between the cave and user area tabs.

The navbar is also responsive to user type. When the user is not logged in, the user area is visible but appears as disabled, prompting the user to log in or sign up. Additionally, only superusers can access the reports tab, which remains invisible to other users.

The mobile version includes the logo and stack bars for the drop-down menu. This version lists the sublinks under the Caves section directly without requiring additional clicks. Similar to the desktop version, the responsiveness to the user's status is also applied.


![Nav Bar](documentation/showcase/nav_bar.png)

<details>
<summary>Nav Bar Effects</summary>

![Nav Bar Effects](documentation/showcase/nav_bar_effects.png)

</details>

<details>
<summary>Nav Bar Privileges - Desktop</summary>

![Nav Bar Privileges - Desktop](documentation/showcase/nav_bar_privliges.png)

</details>

<details>
<summary>Nav Bar Privileges - Mobile</summary>

![Nav Bar Privileges - Mobile](documentation/showcase/nav_bar_privliges_mobile.png)

</details>

[Back to top](#readme---table-of-contents)

#### Footer

I decided not to insert relevant website information in the footer.
Instead, I inserted Font Awesome links to GitHub and LinkedIn.
The footer is very minimalistic, almost imperceptible, as intended.

![Footer](documentation/showcase/footer.png)

[Back to top](#readme---table-of-contents)

#### Home / Index page

The home/index page is comprised of three distinct elements: the hero image, the call-to-action banner linked to a sign-in button (which switches to user area if the user is logged in), and the Cave Metrics section.

The hero image is represented by a panoramic photograph of the Serra do Curral, one of the geomorphological units included in the registry. This range features the Quadrilátero Ferrífero's quartzite and ironstone-supported ridges, with most of the region's caves attributed to the latter. The hero image serves to create visual appeal. In the mobile version, this image is responsive and centers on one of the mountain peaks.

The call-to-action banner aims to inform users about the purpose of the site and intuitively encourage them to register via the button. The text succinctly explains the website's main goals.

![Hero Image and Banner](documentation/showcase/hero_image.png)

![Hero Image and Banner](documentation/showcase/hero_image_mobile.png)

Finally, the Cave Metrics section provides statistical data on caves records, both for the entire Quadrilátero Ferrífero region and the geomorphological units it comprises. This section serves as a valuable reference point for a preliminary assessment of significance. Magnitude ratios are essential for project planning that may affect the speleological heritage. Additionally, these metrics can be integrated into environmental studies without the time-consuming process of consolidating and calculating data, as they are easily accessible through the web application. In the backend, those statistics are run every time there's a request to update the page. I opted not to create a database for this function because this information is dynamic, and there was no need for early optimization as the page's loading time was fast.

![Cave Metrics](documentation/showcase/qf_statistics.png)

The section also includes the total number of caves and those recorded in each geomorphological unit. To ensure greater readability and minimize confusion among the tables, the units are embedded within an accordion. In the mobile version, tables have the overflow-x: scroll attribute for screens smaller than 300px, facilitating the reading of presented values.

![Cave Metrics](documentation/showcase/accordion_geomorphological_units.png)

![Cave Metrics](documentation/showcase/qf_accordion_geomorphological_units_mobile.png)

[Back to top](#readme---table-of-contents)

#### Cave Map Search

The page offers a GIS interface through the Leaflet tool, where users can view the location of caves marked with a custom icon. Clicking on the icon triggers a pop-up displaying general information about the cave, with the cave and user names hyperlinked to their respective individual pages. The page also features a composite altimetry basemap with varying scales, using data from SRTM and even IBGE.

Cave locations are displayed by a function that iterates through all records and returns the geographical coordinates of each cave for the map. In the credits section, links are provided to resources that guided the integration of Django elements into JavaScript functions.

Additional filters can be implemented on this page to optimize the loading speed, but to reach the MVP, such functionalities have been postponed as future features. Nevertheless, the main acceptance criteria for this feature were achieved. To fulfil the requirements of User Story [#6](https://github.com/hpesciotti/Speleometrics/issues/6), a new tool needed to be used, probably ArcGIS web, which would take a long time to implement. I guess the original scope was too convoluted. 

![Map Search Mobile](documentation/showcase/map_search_desktop.png)

![Map Search Mobile](documentation/showcase/map_search_mobile.png)

[Back to top](#readme---table-of-contents)

#### Table Search

The Cave Search allows users to search by exact term, name, or author, or to list caves in ascending and descending order based on metric parameters. This functionality was challenging to implement, and I based it on the work of Joy Zadan (PP5). 

This page offers two distinct versions for cave listing. The search results are displayed in a table on larger screens, while on smaller resolutions, the caves are presented as cards. This approach ensures that search results are easily interpretable on mobile devices. 

As shown on the map page, users can access the specific cave and user pages via hyperlinks. Clicking the links opens the desired page in a new browser tab, allowing users to continue their search seamlessly. Lastly, this page offers options to edit and delete data if accessed by a superuser.

![Cave Search Desktop](documentation/showcase/table_search_user_desktop.png)

<details>
<summary>Cave Search Desktop Privileges - Mobile</summary>

![Cave Search Desktop Privileges - Mobile](documentation/showcase/table_search_admin.png)

</details>

![Cave Search Mobile](documentation/showcase/table_search_mobile.png)

[Back to top](#readme---table-of-contents)

#### About

The About page is the most straightforward page on the site, consisting solely of text and static images. 
Its purpose is to provide general information about the studied area, caves, and environmental licensing, especially regarding the relevance and speleological metrics. At the bottom of the page are external links with the `noopener` attribute to official sources on the topic.

![About Desktop](documentation/showcase/about_desktop.png)

![About Mobile](documentation/showcase/about_mobile.png)

[Back to top](#readme---table-of-contents)

#### Profile

The Profile page includes several checks to ensure the user has filled in their contact email. The contact email is essential for user interaction when requesting information, as described in user stories #10 and #11. On first access, the user is redirected to the profile edit page. After filling it in, users can access the pages to add caves, check their registered caves, or edit their user profile.

![Profile Page - Image](documentation/showcase/profile_page_custom_image.png)

<details>
<summary>Profile Page - No Image</summary>

![Profile Page - No Image](documentation/showcase/profile_page_no_picture.png)

</details>

<details>
<summary>Profile Page - Not logged in</summary>

![Profile Page - Not logged in](documentation/showcase/cave_page_not_logged_in.png)

</details>

[Back to top](#readme---table-of-contents)d)

#### My Caves

Through the profile, users can access "My Caves," which returns their registered caves. The interface is similar to the table search, offering users the option to open individual cave pages, edit the caves, and delete the records. In mobile mode, the table view switches to cards for better presentation.


![Profile Page - Not populated](documentation/showcase/profile_page_my_caves_populated.png)

<details>
<summary>Profile Page - Not populated</summary>

![Profile Page - Not populated](documentation/showcase/profile_page_my_caves.png)

</details>

[Back to top](#readme---table-of-contents)

#### Add Cave / Cave Edit

The "Add Cave" feature is authorized for users whose profiles have a contact email. The function that renders this page checks if the user is logged in (`@login_required`) and if they are the owner of the cave (`profile_user = get_object_or_404(User, username=username)` and `profile = get_object_or_404(Profile, user=profile_user)`). 

The form responsible for adding a cave includes required fields such as `cave_name`, `latitude`, `longitude`, `elevation`, `length`, `depth`, `area`, and `volume`, all of which undergo validation, including Regex checks, to ensure consistent data. If the user fills out a field incorrectly, the form returns a custom alert message indicating where the error occurred. It's worth mentioning that despite the option to upload a cave map, no maps have been added to the current cave records (although one appears in the screenshots). This is because materials such as cave sketches and photos are often provided to mining companies under non-disclosure agreements, which unfortunately prevents me from attaching such data at this time. Lastly, the same form used in `cave_add` is also utilized for editing cave data (`cave_edit`), but the function that renders it retrieves the cave data and populates each field accordingly.

Through the profile, users can access "My Caves," which returns their registered caves. The interface is similar to the table search, offering users the option to open individual cave pages, edit the caves, and delete the records. In mobile mode, the table view switches to cards for better presentation.


![Register Cave](documentation/showcase/register_cave.png)

<details>
<summary>Register Cave - No Filled</summary>

![Register Cave - No Filled](documentation/showcase/register_cave_wont_proceed.png)

</details>

<details>
<summary>Register Cave - Error</summary>

![Register Cave - Error](documentation/showcase/register_cave_error_notifications.png)

</details>

[Back to top](#readme---table-of-contents)

#### Cave Page

The cave page consists of a simple layout where the data is presented individually in a textual format. On this page, the owner of the cave has the option to delete it. Conversely, any user can submit a report for inconsistencies. This report is submitted through a modal equipped with a text box where the reporting user only needs to fill in the specific inconsistency found in the data. The other data points, such as `cave`, `reported_by`, `cave_owner`, and `reported_created_date`, are automatically collected.

![Cave Page](documentation/showcase/cave_page_not_logged_in.png)

<details>
<summary>Cave Page - Notification</summary>

![Cave Page - Notification](documentation/showcase/cave_page_notitification.png)

</details>

<details>
<summary>Cave Page - Delete Modal</summary>

![Cave Page - Delete Modal](documentation/showcase/delete_cave_modal.png)

</details>

[Back to top](#readme---table-of-contents)

#### Report

The report page is restricted to superusers. Its purpose is to list records with inconsistent data. This page includes filtering options to allow site administrators to organize review requests and provide the necessary follow-up. Each item can be viewed separately using the "Detail" button. 

At the end of the review process, the admin can delete the review request. At this stage of the website, there is no automated way for the user to track if their report request has been addressed, except through email communication from the administrator.

![Report](documentation/showcase/report.png)

![Report Page](documentation/showcase/report_page.png)

[Back to top](#readme---table-of-contents)

#### Sign In Page

The sign In page is supported by Django AllAuth model. 
I added some personalisation to return erro messages.

![SignIn Validation 1](documentation/showcase/sign_in_validation.png)

![SignIn Validation 2](documentation/showcase/sign_in_validation_2.png)

[Back to top](#readme---table-of-contents)

#### Error pages
The website has custom pages for the following errors:
- 403 - Forbidden
- 404 - Not Found
- 500 - Internal Server Error

### **3.4. Future Features**

- Extended user management panel with profile viewing and editing capabilities.
- Disable, delete, or temporarily suspend user accounts due to misuse.
- Restore disabled or suspended accounts and track account management history.
- Add more filering options to Cave model fields.

[Back to top](#readme---table-of-contents)

## **4. Technologies Used**

### **4.1. Languages Used**

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

- [Python](https://www.python.org/about/)

- [JavaScript](https://www.javascript.com/)

[Back to top](#readme---table-of-contents)

### **4.2 - Frameworks, Libraries, Technologies & Programs Used**  

- [Gitpod](https://www.gitpod.io): used form coding

- [GitHub](https://github.com/): to save and store all files for this web application 

- [Git](https://git-scm.com/): used for version control

- [Django](https://www.djangoproject.com/): for building the web application

- [Regex](https://www.w3schools.com/python/python_regex.asp): for checking for pattern in strings.

- [Google Fonts](https://fonts.google.com/): font was imported from here 

- [Font Awesome](https://fontawesome.com/): icons and their associated kit were downloaded from here  

- [Leaflet](https://leafletjs.com/examples.html): an open-source JavaScript library for mobile-friendly interactive maps, especially the tutorials section on how to how to add a marker and set custom style for the marker.

- [Numpy](https://numpy.org/): for running the statistics

- [Cloudinary](https://cloudinary.com/): for storing images (cave-maps and profile pictures)

- [Microsoft Power Point](https://www.lucidchart.com/pages/?): used to create data chart and logo

- [ChatGPT](https://chat.openai.com/): for improving and making text content more engaging.

- [ArcGIS](https://www.arcgis.com/index.html): to build the QF geomorphological units map.

- [Grammarly](https://app.grammarly.com): for spelling or grammatical inaccuracies in the text

- [Google Chrome Lighthouse](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk): for auditing the performance of the web application

- [Code Institute Linter](https://pep8ci.herokuapp.com/#): for validating Python code according PEP 8

- [MS Paint](https://www.microsoft.com/en-us/windows/paint): for editing the captured screenshots

- [Heroku](https://dashboard.heroku.com/): for deploying the terminal application.

[Back to top](#readme---table-of-contents)

## **5. Testing**

- An additional file for Testing can be found here: [Testing](https://github.com/hpesciotti/Speleometrics/blob/main/TESTING.md)

## **6. Deployment**

The website was developed using Gitpod code editor, committed to Git as a local repository, and then pushed to GitHub for storage.

## **6.1 Code Institute PostgreSQL Database**

- Navigate to [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net/)
- Enter your student email address in the input field provided.
- Wait for database to be created and review the email sent to your student email inbox.

[Back to top](#readme---table-of-contents)

### **6.2. Connecting to GitHub**

To begin this project from scratch, you must first create a new GitHub repository using the [Code Institute's Template](https://github.com/Code-Institute-Org/ci-full-template). This template provides the relevant tools to get you started. To use this template:

1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above CI Full Template.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new repository name and click '**Create repository from template**'.
5. In Gitpod locate your repository and create a new workspace.

[Back to top](#readme---table-of-contents)

### **6.3. Django Project Setup**

- Install Django and all supporting libraries for Speleometrics: 

```
pip install asgiref==3.8.1
pip install cloudinary==1.36.0
pip install dj-database-url==0.5.0
pip install dj3-cloudinary-storage==0.0.6
pip install Django==4.2.16
pip install django-allauth==0.57.2
pip install django-resized==1.0.2
pip install django-summernote==0.8.20.0
pip install gunicorn==20.1.0
pip install numpy==2.1.2
pip install oauthlib==3.2.2
pip install pillow==10.4.0
pip install psycopg2==2.9.9
pip install PyJWT==2.9.0
pip install python3-openid==3.2.0
pip install requests-oauthlib==2.0.0
pip install sqlparse==0.5.1
pip install urllib3==1.26.20
pip install whitenoise==5.3.0
```
  
- After the insatalation process run ```pip3 freeze --local > requirements.txt``` in the terminal.  
- Create a new Django project in the terminal ```django-admin startproject speleometrics .```
- Create a new app eg. ```python3 mangage.py startapp caves```
- Register caves in **INSTALLED_APPS** in **settings.py** as 'caves',
- Run ```python3 manage.py createsuperuser``` and enter credentials to create a superuser, allowing Admin access.
- Run migrations with commands: ```python3 manage.py makemigrations``` and ```python3 manage.py migrate```
- Create an **env.py** to store all confidential data such as the **DATABASE_URL** and **SECRET_KEY**. 

```import os
os.environ["DATABASE_URL"]="<CI's data base>"
os.environ.setdefault("CLOUDINARY_URL")
```

- Add envy.py to must be added to your **gitignore**, so it will not be upload to GitHub.
- Reference the file in your project's **settings.py**: 
For adding to **settings.py**:

```
import os
import dj_database_url
if os.path.exists("env.py"):
import env
```

- Replace **DATABASES** with:

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
```

- Set up the templates directory in **settings.py**:
    Under ``BASE_DIR`` enter ``TEMPLATES_DIR = os.path.join(BASE_DIR, ‘templates’)``
    Update ``TEMPLATES = 'DIRS': [TEMPLATES_DIR]`` with:

```
os.path.join(BASE_DIR, 'templates'),
os.path.join(BASE_DIR, 'templates', 'allauth')
```

- Create the media, static and templates directories in top level of project file in IDE workspace.

-  Create a Procfile in the project repository for Heroku deployment, containing the following line:
web: gunicorn speleometrics.wsgi

-  Run migrations again to ensure all database changes are applied.

[Back to top](#readme---table-of-contents)


### **6.4. Cloudinary API**

Cloudinary offers a cloud-based solution for media storage. All images uploaded by users in the Speleometrics project are hosted on this platform.

To get started, create a new account at Cloudinary and add your Cloudinary API environment variable to your env.py file and Heroku Config Vars. In your project workspace:
  - Include the Cloudinary libraries in the INSTALLED_APPS section of your settings.py file, in the following order:
```
   'cloudinary_storage',  
   'django.contrib.staticfiles',  
   'cloudinary',
```
- Add to **env.py** and link up with **settings.py**: ```os.environ["CLOUDINARY_URL"]="cloudinary://...."``` 
- Configure Cloudinary as the storage for media and static files in settings.py with the following settings:

```
STATIC_URL = '/static/
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'  
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]  
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')‌  
MEDIA_URL = '/media/'  
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```
[Back to top](#readme---table-of-contents)

### **6.5. Heroku Deployment**

To start the deployment process , please follow the below steps:

- Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user.
- Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create New App**'.
- Enter an app name and choose your region. Click '**Create App**'. 
-  In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. The KEY:VALUE pairs that you will need are your: 
   
   - Set CLOUDINARY_URL** 
   - Set DATABASE_URL**
   - Set DISABLE_COLLECTSTATIC to 1
  
- Add the Heroku host name into **ALLOWED_HOSTS** in your projects **settings.py file** -> ```['herokuappname', ‘localhost’, ‘8000 port url’].```
- Once you are sure that you have set up the required files including your requirements.txt and Procfile, you have ensured that **DEBUG=False**, save your project, add the files, commit for initial deployment and push the data to GitHub.
- Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
- Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
-  Choose from '**Automatic**' or '**Manual**' deployment options, I chose the 'Manual' deployment method. Click '**Deploy Branch**'.
- Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site. If you receive any errors, Heroku will display a reason in the app build log for you to investigate. *

[Back to top](#readme---table-of-contents)

### **6.6. Make a Local Clone Project**

A local clone of this repository can be made on GitHub. Please follow the below steps:

- Navigate to GitHub and log in.
- The [Speleometrics](https://github.com/hpesciotti/Speleometrics/) can be found at this location.
- Above the repository file section, locate the '**Code**' button.
- Click on this button and choose your clone method from HTTPS, SSH or GitHub CLI, copy the URL to your clipboard by clicking the '**Copy**' button.
- Open your Git Bash Terminal.
- Change the current working directory to the location you want the cloned directory to be made.
- Type `git clone` and paste in the copied URL from step 4.
- Press '**Enter**' for the local clone to be created.
- Using the ``pip3 install -r requirements.txt`` command, the dependencies and libraries needed for FreeFido will be installed.
- Set up your **env.py** file and from the above steps for Cloudinary and ElephantSQL, gather the Cloudinary API key and the Elephant SQL url for additon to your code.
- Ensure that your **env.py** file is placed in your **.gitignore** file and follow the remaining steps in the above Django Project Setup section before pushing your code to GitHub.

[Back to top](#readme---table-of-contents)


### **6.7. Clone Project**

A copy of the original repository can be made through GitHub. Please follow the below steps to fork this repository:  

- Navigate to GitHub and log in.  
- Once logged in, navigate to this repository using this link [Speleometrics](https://github.com/hpesciotti/Speleometrics/).
- Above the repository file section and to the top, right of the page is the '**Fork**' button, click on this to make a fork of this repository.
- You should now have access to a forked copy of this repository in your Github account.
- Follow the above Django Project Steps if you wish to work on the project.

[Back to top](#readme---table-of-contents)

## **7. Credits**

### **7.1. Content**

- Code Institute - I think there for I Blog project: Django walkthrough project.

- [RegexTutorial](https://www.regextutorial.org/positive-and-negative-lookahead-assertions.php): reading material on negative and positive lookahead assertions

- [W3Schools](https://www.w3schools.com/python/python_regex.asp): for Regex reading material.

- [Regex Calculator](https://regex101.com/): for testing and implementing Regex

- [Django Docs](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.readonly_fields): For general info on Django functionalites

- [Leaflet](https://leafletjs.com/examples.html): an open-source JavaScript library for mobile-friendly interactive maps, especially the tutorials section on how to how to add a marker and set custom style for the marker.

- [D3noob GitHub page](https://gist.github.com/d3noob/9150014): how to add multiple points to leaflet div's map.

- [Leaflet Basemap Previw](https://leaflet-extras.github.io/leaflet-providers/preview/): To pick a basemap for cave_maps page.

- [Geographic Information Systems](https://gis.stackexchange.com/questions/184125/alternative-basemaps-for-leaflet): for info on alternative basemaps for Leaflet.

- [appsbd](https://appsbd.com/how-to-create-map-using-leaflet-js-best-way-to-figure/): On how to add pop-ups to Leaflet.

- [Stack Overflow](https://stackoverflow.com/questions/63962443/create-a-post-save-signal-that-creates-a-profile-object-for-me): Creating post signals.

- [Stack Overflow](https://stackoverflow.com/questions/14820952/change-bootstrap-input-focus-blue-glow): Changing glow default glow effects on bootstrap.

- [Stack Overflow](https://stackoverflow.com/questions/7168658/why-is-the-padding-not-working-on-my-label-elements): Setting padding to input fields.

- [Stack Overflow](https://stackoverflow.com/questions/8806673/html-how-to-retain-formatting-in-textarea): on how to retain formatting o text area.

- [Boostrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/): Implementing nav bar, accordion, focus, hover effects, grid structure and more.

- [Amy Richardson](https://github.com/amylour/FreeFido_v2): for post signals and general django structure.

- [Joy Zadan](https://github.com/JoyZadan/shop-kbeauty): Implementing search bar and filters.

- [StaticsGlobe](https://www.youtube.com/watch?v=VZAmgg_khO0): How to calculate percentiles with num.py

[Back to top](#readme---table-of-contents)


### **7.2. Media**

- [Font Awesome](https://fontawesome.com/): for the icons used in the footer of the application.

- [Unplash](https://unsplash.com/pt-br/s/fotografias/Serra-do-Curral): for index hero image

- All remaining photographs are my own.

[Back to top](#readme---table-of-contents)

### **7.3. Acknowlegements**

- My informal mentor and great friend, [Bruno Dias](https://github.com/brunoald/), for helping me to structure the project.

- My mentor, Darío Carrasquel, for his support and constructive feedback.

- My partner, Joana, for all the emotional support.

[Back to top](#readme---table-of-contents)

