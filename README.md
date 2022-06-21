# WePlayWeb
## MySQL Setup
#### Create Database
`CREATE DATABASE weplayweb;`
#### Select Database
`use weplayweb;`
## Create a Table 
### Home Page Table
###### Table Name : HomePage
`CREATE TABLE HomePage (Section char(4),Heading varchar(255), Paragraph LONGTEXT;`

###### Example Query Structure
`INSERT INTO HomePage (Section,Heading,Paragraph) VALUES ("H1","One place.For all your digital marketing experience","We provide you the best in class products with complete satisfaction.");`
###### Example Table Structure

|  Section |Heading   | Paragraph    |
| ------------ | ------------ | ------------ |
|  H1 | One place.For all your digital marketing experience  |  We provide you the best in class products with complete satisfaction. |
|  H2 |5 Years Experience   | Due to the increasing demand for cloud, most of them are marching towards web based applications. Those applications will be excellent when developed with creativity and smartness. We are experts in web designing and development on whom you can rely on. Software development is a collection of several modules put together to provide the expected result. Whatever the requirement you may have, we take the responsibility of offering the perfect software for you.  |
|  H3 |  Web Design And Hosting |  Lorem ipsum dolor sit amet elit. Phasellus nec pretium mi. Curabitur facilisis ornare |
|  H4 |  Ethical Hacking Training |  Lorem ipsum dolor sit amet elit. Phasellus nec pretium mi. Curabitur facilisis ornare |
|  H5 | MiddleWare integration  |  Lorem ipsum dolor sit amet elit. Phasellus nec pretium mi. Curabitur facilisis ornare |
|  H6 |  Workshops and Hands-on training |  Lorem ipsum dolor sit amet elit. Phasellus nec pretium mi. Curabitur facilisis ornare |
|  H7 |  Expert Cleaners and World Class Services  |  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec pretium mi. Curabitur facilisis ornare velit non vulputate. Aliquam metus tortor, auctor id gravida condimentum, viverra quis sem. Curabitur non nisl nec nisi scelerisque maximus. Aenean consectetur convallis porttitor. Aliquam interdum at lacus non blandit. |
|  H8 |  Business specific Service | We have different models of projects for different Business streams.  |
|  H9 | Digital Branding  |  We help you to build your brand in Digital market. Your presence in Web will increase your business. |
| H10| Social media Marketing  | We also help you to build your brand through social media which is a great source of customers.  |




### About Page Table
###### Table Name : AboutPage
`CREATE TABLE AboutPage (Section char(4),Heading varchar(255), Paragraph LONGTEXT;`
### Service Page Table
###### Table Name : ServicePage
`CREATE TABLE ServicePage (Section char(4),Heading varchar(255), Paragraph LONGTEXT;`
### Contact Page Table
###### Table Name : ContactPage
`CREATE TABLE ContactPage (Section char(4),Heading varchar(255), Paragraph LONGTEXT;`

### To Display all Table in Database
`SHOW TABLES;`
