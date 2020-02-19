from zomato_search_result import ZomotoSearchResult

import smtplib

def initialize_app(config):
    # creates SMTP session 
    return SentEmail(config)
    
class SentEmail:

    def __init__(self, config):
        self.smtp_host = config['host']
        self.smtp_port = config['port']
        self.sender_email_id = config['sender_email_id']
        self.sender_email_id_password = config['sender_password']

    def sent_email(self, email_id, location, cuisine, average_budget, results: ZomotoSearchResult):
        try:
            smtp = smtplib.SMTP(self.smtp_host, self.smtp_port)

            smtp.ehlo()
                
            # start TLS for security 
            smtp.starttls() 
        
            # Authentication 
            smtp.login(self.sender_email_id, self.sender_email_id_password) 
        
            # message to be sent 
            message = self.create_message(self.sender_email_id, email_id, location, cuisine, average_budget, results)
        
            # sending the mail 
            smtp.sendmail(self.sender_email_id, email_id, message) 
        
            # terminating the session 
            smtp.quit()

            return True
        except:
            return False

    def create_message(self, sender_email_id, receiver_email_id, location, cuisine, average_budget, results):
        response = 'Here are your {} restaurants in {} for {} budget:\n'.format(cuisine, location.title(), average_budget)
        for index, result in enumerate(results):
            output = '{}) {} in {} has been rated {} having average budget of Rs. {}'.format((index  + 1), result.restaurant_name,
            result.restaurant_address, result.user_rating, result.avg_budget_for_two)
            response = response + output +"\n"

        message = "\r\n".join([
            "From: {}",
            "To: {}",
            "Subject: Requested top 10 {} restaurants in {} for {} budget:\n".format(cuisine, location.title(), 
            average_budget),
            "",
            "{}"
            ]).format(sender_email_id, receiver_email_id, response)
        
        return message