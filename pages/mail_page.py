import email
import imaplib
import random
import re
import string
import time
import logging
from email.header import decode_header
from pages.base_page import BasePage

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MailPage():

    def generate_random_email(self, original_email, number_of_symbols_to_add=8):
        splitted_email = original_email.split('@')
        letters_and_digits = string.ascii_letters + string.digits
        result_str = ''.join((random.choice(letters_and_digits) for i in range(number_of_symbols_to_add)))
        new_email = splitted_email[0] + "+" + result_str + "@" + splitted_email[1]
        return new_email

    def clear_mailbox(self, email, password):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(email, password)
        mail.list()
        # Выводит список папок в почтовом ящике.
        mail.select("inbox")  # Подключаемся к папке "входящие".
        result, data = mail.search(None, "ALL")
        messages = data[0].split()  # Разделяем ID писем
        for one_mail in messages:
            mail.store(one_mail, "+FLAGS", "\\Deleted")  # mark the mail as deleted

        mail.expunge()  # permanently remove mails that are marked as deleted from the selected mailbox (in this case, INBOX)
        mail.close()  # close the mailbox

    def wait_email_to_come(self, mail, number_of_tries=50, waiting_time=1):
        logging.info("wait_email_to_come--------------------------")

        for tries in range(number_of_tries):
            mail.list()  # Выводит список папок в почтовом ящике.
            mail.select("inbox")  # Подключаемся к папке "входящие".  
            logging.info("tryyy--------------------------" + str(tries))
            result, data = mail.search(None, "ALL")
            id_list = data[0].split()  # Разделяем ID писем
            logging.info(len(id_list))
            if len(id_list) != 0:
                return True
            time.sleep(waiting_time)
        return False

    def get_link_from_message(self, email, password, number_of_tries=20, waiting_time=1):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(email, password)

        if self.wait_email_to_come(mail) == True:
            mail.list()  # Выводит список папок в почтовом ящике.

            mail.select("inbox")  # Подключаемся к папке "входящие".    
            result, data = mail.search(None, "ALL")
            id_list = data[0].split()
            latest_email_id = id_list[-1]  # Берем последний ID
            result, data = mail.fetch(latest_email_id, "(RFC822)")  # Получаем тело письма (RFC822) для данного ID
            raw_email = data[0][1]  # Тело письма в необработанном виде
            raw_email = raw_email.decode("utf-8").replace('=\r\n', '')
            mail_link = re.search(
                r'https://((\w+\.\w+\.\w+)|(\w+\.\w+))[/](\w{2}-\w{2,3}|\w{2,7})/verify/email/(\d+)[/](\w+)', raw_email)
            logging.info("Link detected "+mail_link.group())
            return mail_link.group()
        else:
            assert "Error, message is not found"
