Django REST Framework Invoice API

This Django application provides RESTful APIs for managing invoices and their details.

Features:

Single URL endpoint /invoices/ for managing invoices
Models: Invoice and InvoiceDetail
Invoice fields: Date, Customer Name
InvoiceDetail fields: Invoice (ForeignKey), Description, Quantity, Unit Price, Price
APIs support all HTTP methods for CRUD operations on invoices
APIs accept invoice details in the payload for creating/updating associated invoice details
Includes test cases to ensure API functionality
API Endpoints:

GET /invoices/
Retrieves a list of all invoices


POST /invoices/
Creates a new invoice


GET /invoices/{invoice_id}/
Retrieves details of a specific invoice


PUT /invoices/{invoice_id}/
Updates details of a specific invoice


DELETE /invoices/{invoice_id}/
Deletes a specific invoice

Setup:

Clone the repository:

bash
Copy code
git clone <repository_url>
Install dependencies:

Copy code
pip install -r requirements.txt
Run migrations:

Copy code
python manage.py migrate
Start the development server:

Copy code
python manage.py runserver
Testing:

Run test cases:
bash
Copy code
python manage.py test
Endpoints Usage:

Use your favorite API client (e.g., Postman) to interact with the API endpoints.
Send requests to the specified endpoints with appropriate payloads to create, update, delete, and retrieve invoices.
Contributing:

Contributions are welcome! Feel free to submit issues or pull requests to improve the application.

Author:

Nutan Mali - nutansm123@gmail.com
