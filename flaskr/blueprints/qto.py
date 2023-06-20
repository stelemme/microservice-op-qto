from flask import (
    Blueprint, render_template, request, make_response, jsonify
)
import rdflib
from collections import Counter

# Initiating the blueprint and assigning to it the "/op/" URI
bp = Blueprint('qto', __name__, url_prefix='/op')

# Adding a function to the "/op/some-operation" URI
@bp.route('/qto', methods=('GET', 'POST'))
def operation():
    if request.method == 'GET':
        response = make_response({
            "supported_methods": ["GET", "POST"],
            "POST_request_data": "text/turtle",
            "POST_response_data": "application/ld+json",
        })

        return response

    elif request.method == 'POST':
        # The data is retrieved out of the incoming HTTP POST request.
        file = request.data

        try:
            # Here some operation happens on the data.
            g = rdflib.Graph()
            g.parse(file, format='turtle')
            sparql_results = g.query("""
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX bot: <https://w3id.org/bot#>
                PREFIX props: <http://lbd.arch.rwth-aachen.de/props#>

                SELECT ?element ?globalId ?name ?objectType ?storey
                WHERE {
                    ?element rdf:type bot:Element ;
                        props:globalIdIfcRoot_attribute_simple ?globalId ;
                        props:nameIfcRoot_attribute_simple ?name ;
                        props:objectTypeIfcObject_attribute_simple ?objectType ;
                }
            """)

            qto = {
                "@context": {
                    "props": "http://lbd.arch.rwth-aachen.de/props#",
                    "bot": "https://w3id.org/bot#",
                    "schema": "http://schema.org/",
                    "quantity": {
                        "@id": "schema:Quantity",
                        "@type": "schema:Integer"
                    }
                },
                "@type": "schema:ItemList",
                "schema:itemListElement": []
            }

            objects = [row[3] for row in sparql_results]
            objects.sort()

            elements_count = Counter(objects)

            qto["schema:itemListElement"] = [
                {"@type": "bot:Element", "props:objectTypeIfcObject_attribute_simple": element,  "quantity": count} 
                for element, count in elements_count.items()
            ]
            

            # The response data is added to the response
            response = make_response(qto)
            response.headers['Content-Type'] = 'application/ld+json'

            # The response code is set, and the response is sent back to the requesting party.
            response.status_code = 200
            return response
        
        except Exception as e:
            # Return an error response if the file cannot be parsed
            error_message = f"Error while performing QTO"
            error_response = {'error': error_message}
            return jsonify(error_response), 400
    
    


