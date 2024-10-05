# Job Portal Backend (Django)
>This repository contains the backend API for a Job Portal application, built using **Django** and **Django REST Framework**. It provides distinct functionalities for job seekers, companies, and platform administrators. This backend supports data management, authentication, and API endpoints for job listings, applications, and user profiles.  
`Frontend (React)` 👉 [Job Portal Frontend](https://github.com/sravan-kumar-ta/Job-portal-React.git)


## Features

### Job Seeker
- **Profile Management**: Create, update, and manage your profile, including resume and work experience.
- **Job Listings**: View and filter job listings with options for pagination and sorting.
- **Job Applications**: Apply for jobs and track the status of applications.

### Company
- **Company Profile Management**: Create and update company profiles.
- **Job Management**: Create, update, and list jobs posted by the company.
- **Application Management**: View and manage job applications for positions listed by the company.

### Admin
- **Admin Dashboard**: Overview of the total number of job seekers, companies, and other platform statistics.
- **Company Approvals**: Review and approve new company registrations.
- **User Management**: Manage all user accounts on the platform, including job seekers and companies.

## Tech Stack

<table>
    <tr>
        <td align="center">
            <img height="40"
                src="https://github.com/marwin1991/profile-technology-icons/assets/62091613/9bf5650b-e534-4eae-8a26-8379d076f3b4">
            <br>Django
        </td>
        <td align="center">
            <img height="40"
                src="https://user-images.githubusercontent.com/25181517/192107858-fe19f043-c502-4009-8c47-476fc89718ad.png">
            <br>REST
        </td>
        <td align="center">
            <img height="40"
                src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original.svg">
            <br>PostgreSQL
        </td>
    </tr>
</table>

- **Backend Framework**: Python-Django
- **API**: Django REST Framework
- **Authentication**: JWT (JSON Web Tokens) using `rest_framework_simplejwt`
- **Token Blacklisting**: Simple JWT Token Blacklist
- **CORS Handling**: Django CORS Headers
- **Database**: PostgreSQL
- **Pagination and Filtering**: Django REST Framework's `SearchFilter`, `OrderingFilter`, and `PageNumberPagination`

## Screenshots
<table>
    <tr>
        <td style="padding: 20px 30px;">
            <img height="300"
                src="https://github.com/user-attachments/assets/9b3984f6-46ae-4e7d-a1d5-4e616998137e">
        </td>
        <td style="padding: 20px 30px;">
            <img height="300"
                src="https://github.com/user-attachments/assets/90e1b6f6-fb6b-4a81-88dc-303ad63169f5">
        </td>
    </tr>
    <tr>
        <td style="padding: 20px 30px;">
            <img height="300"
                src="https://github.com/user-attachments/assets/21bd4543-ae27-4818-87be-6716b47b59b3">
        </td>
        <td style="padding: 20px 30px;">
            <img height="300"
                src="https://github.com/user-attachments/assets/e7132f79-869d-4628-ac65-86f68fc5f347">
        </td>
    </tr>
    <tr>
        <td style="padding: 20px 30px;">
            <img height="300"
                src="https://github.com/user-attachments/assets/397a9e6e-ca14-45c2-86f8-f372082d7826">
        </td>
        <td style="padding: 20px 30px;">
            <img height="300"
                src="https://github.com/user-attachments/assets/d7b0ea32-4ac8-463a-a7ba-3b2d6146d277">
        </td>
    </tr>
</table>

-----