import mercadopago
import os
import uuid

def gerar_link_pagamento():
    
	sdk = mercadopago.SDK(os.getenv("MP_ACCESS_TOKEN"))

	request = {
		"items": [
			{
				"id": "1",
				"title": "Currículo",
				"quantity": 1,
				"currency_id": "BRL",
				"unit_price": 20,
			},
		],
		"payer": {
			"name": "User1",
			"surname": "User1Sur",
			"email": "your_test_email@example.com",
			"phone": {
				"area_code": "11",
				"number": "4444-4444",
			},
			"identification": {
				"type": "CPF",
				"number": "19119119100",
			},
			"address": {
				"zip_code": "06233200",
				"street_name": "Street",
				"street_number": 123,
			},
		},
		"back_urls": {
			"success": "http://127.0.0.1:5000/success",
			"failure": "http://127.0.0.1:5000/failure",
			"pending": "http://127.0.0.1:5000/pending",
		},
		"auto_return": "all",
	}

	preference_response = sdk.preference().create(request)
	preference = preference_response["response"]
	return	preference['sandbox_init_point']