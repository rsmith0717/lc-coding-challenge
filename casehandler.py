import traceback
from PPPForgivenessSDK.client import Client


class CaseHandler():
    def __init__(self):
        self.client = Client(
            access_token='c1fad04273b482eba7c8e14c4db57479defbbfc7',
            vendor_key='2139dbe1-3fca-4729-9d29-724cd3d63672',
            environment='sandbox'
        )

    def create_forgivness_request(self, sba_number: int, funding_date: str, etran_notational_amount: float, 
        bank_notational_amount: float, ein: str, entity_name: str):
        """Create a new forgiveness request using sba_number, funding date, etran notational amount, bank notational amount, ein, and entity name."""
        try:
            response = self.client.forgiveness_requests.create(
                bank_notional_amount=bank_notational_amount,
                sba_number=int(sba_number),
                loan_number=int('12311'),
                entity_name=entity_name,
                ein=ein,
                funding_date=funding_date,
                forgive_payroll= 1000.00,
                forgive_eidl_amount = 100.00,
                forgive_eidl_application_number= 123456789,
                naics_code= 722513,
                ppp_loan_draw =  1,
                address1 = "154 Test Ln – Suite Z",
                address2 = "Birmingham, AL",
                dba_name = "Testing Inc",
                phone_number= "6102342123",
                forgive_fte_at_loan_application = 10,
                demographics = [],
                forgive_amount = 1666.66,
                forgive_fte_at_forgiveness_application = 10,
                forgive_covered_period_from = "2020-07-06",
                forgive_covered_period_to = "2020-09-06",
                forgive_2_million = False,
                primary_email = "anotheruser@example.com",
                primary_name = "Testerson",
                ez_form = False,
                forgive_lender_confirmation = True,
                forgive_lender_decision = 1,
                s_form = True
            )

            if response['status'] == 201:
                print(response['data'])
                self.upload_forgiveness_files()
            else:
                print("An error occurred." + str(response['status']))
                print(response['data'])
                # The request always errors out. I'm assuming this is the data will not work part of the challenge.
                # run upload forgiveness files function on error only for demonstration purposes.
                self.upload_forgiveness_files()
        except Exception as e:
            print(traceback.format_exc())
            return None


    def delete_forgiveness_request(self, slug: str):
        """ Delete a forgiveness request by using the slug supplied as a string. """
        try:
            result = self.client.forgiveness_requests.delete(slug=slug)

            if result['status'] == 204:
                print('deleted')
            else:
                print("An error occurred." + str(result['status']))
                print(result['data'])
        except Exception as e:
            print(traceback.format_exc())
            return None

    def upload_forgiveness_files(self, files: list=None):
        """ Uploads files with a list of dictionaries containing file information. """
        file_upload = self.client.loan_documents
        uuid = 'df481fbb-c41f-46f3-b96f-94374d747a8d'

        document1 = {"name": "Payroll.pdf", "type": 1, "path": './Form3508S.pdf'}
        document2 = {"name": "DenialJustification.pdf", "type": 3, "path": './Form3508S.pdf'}
        document3 = {"name": "MiscellaneousDoc1.pdf", "type": 9, "path": './Form3508S.pdf'}

        # create list of documents from potential multi part file upload
        if files:
            documents = files
        else:
            documents = [document1, document2, document3]
        print("The documents are: ", documents)

        if documents:
            for document in documents:
                # upload documents
                try:
                    response = file_upload.create(document.get('name','default'), document.get('type',1), uuid, document.get('path', ''))
                    print("The response is: ", response)

                    if response['status'] == 201:
                        print(response['data'])
                    else:
                        print("An error occurred." + str(response['status']))
                        print(response['data'])
                except Exception as e:
                    print(traceback.format_exc())
                    return None
        else:
            print("No documents found.")
            return None


    def lookup(self, sba_number: str=None):
        """ Lookup the loan using the sba number. """
        if sba_number:
            try:
                response = self.client.validations.list(sba_number=str(sba_number))
                
                if response['status'] == 200:
                    print(response['data'])
                    return response['data']
                else:
                    print("An error occurred." + str(response['status']))
                    print(response['data'])
            except Exception as e:
                print(traceback.format_exc())
                return None
        else:
            print("No sba number given")
            return None

def handle_case1(sba_number: int=405849734124238, funding_date: str='2020-05-23', etran_notational_amount: float=6829869.75, 
    bank_notational_amount: float=6829869.75, ein: str=380753125, entity_name: str='Mock Business'):
    """ Handles case 1 using the CaseHandler class """
    case_handler = CaseHandler()
    case_handler.create_forgivness_request(sba_number, funding_date, etran_notational_amount, bank_notational_amount, ein, entity_name)

def handle_case6(sba_number: str="405849734124238"):
    """ Handles case 6 using the CaseHandler class """
    case_handler = CaseHandler()
    case_handler.lookup(sba_number)

handle_case1()
handle_case6()