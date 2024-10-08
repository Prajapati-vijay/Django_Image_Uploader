# Django_Image_Uploader
This project is a simple Django application that allows users to upload images. It uses Django Rest Framework for creating a RESTful API and supports CRUD operations on the uploaded images.

## Technologies Used

- Django
- Django Rest Framework
- Python
- SQLite (or any other database)

## Installation

### Prerequisites

Ensure you have the following installed on your system:

- Python (3.x)
- pip (Python package installer)
- Django (3.x or above)
- Django Rest Framework

### Steps to Install

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/image-uploader.git
   cd image-uploader
   ```
2. **Create a Virtual Environment (optional but recommended)**:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install Dependencies**:

```
pip install -r requirements.txt
```

4. **Set Up the Database: Run the following commands to apply migrations and create the database**:

```

python manage.py migrate

```
5. ***Create a Superuser (optional): To access the Django admin panel, you can create a superuser**:

```
python manage.py createsuperuser
```

6. **Run the Development Server: Start the Django development server**:

```
python manage.py runserver

```
7. **Access the Application: Open your web browser and go to**:

```
http://127.0.0.1:8000/

```


## API Endpoints

# List Images: GET /images/
# Upload Image: POST /images/
# Retrieve Image: GET /images/{id}/
# Update Image: PUT /images/{id}/
# Delete Image: DELETE /images/{id}/


