import requests
import re
import logging


class WorkWithAdminPage():

    def check_platform(self,platform):
        if platform == "dev":
            link = "https://dev."
        else:
            link = "https://"
        return link
    def login_to_admin(self, admin_user_login, admin_user_password,platform):
        '''
        :param admin_user_login: Логин юзера админки
        :param admin_user_password: Пароль юзера админки
        :return: Аксес-токен юзера, Айди юзера
        '''
        sign_in_url = self.check_platform(platform)+"admin.slotoboss.com/platform/user/admin/auth/sign-in"
        sign_in_payload = "{\"login\":\"" + admin_user_login + "\",\"password\":\"" + admin_user_password + "\"}"
        sign_in_headers = {'Content-Type': 'application/json; charset=UTF-8'}
        authorize = requests.request("POST", sign_in_url, headers=sign_in_headers, data=sign_in_payload)
        query_id = re.search(r'id\":\"\d{5,6}', authorize.text)
        admin_user_id = re.findall('[0-9]+', query_id.group())[0]
        logging.info( str(admin_user_id))
        return ([authorize.headers['Access-Token'], str(admin_user_id)])

    def switch_user_to_test(self, admin_user_login, admin_user_password, user_email,platform):
        finded_user=self.find_userID_by_email(admin_user_login, admin_user_password, user_email,platform)
        user_id = str(finded_user[0])
        token_id_pair = finded_user[1]

        make_user_test_url = self.check_platform(platform)+"admin.slotoboss.com/platform/user/admin/players/change-user-is-test"
        make_user_test_payload = "{ \"id\": \"" + user_id + "\" }"
        make_user_test_headers = {'Token-Type': "Bearer", 'Access-Token': token_id_pair[0], 'uid': token_id_pair[1],
                                  'Content-Type': 'application/json; charset=UTF-8', 'client': 'user'}
        make_user_test_result = requests.request("POST", make_user_test_url, headers=make_user_test_headers,
                                                   data=make_user_test_payload)

        logging.info("Is user test result"+str(make_user_test_result.json()))

    def find_userID_by_email(self, admin_user_login, admin_user_password, user_email,platform):
        token_id_pair = self.login_to_admin(admin_user_login, admin_user_password,platform)
        find_user_url = self.check_platform(platform)+"admin.slotoboss.com/platform/user/admin/players/find"
        find_user_payload = "{\"account\": { \"lastLogin\": {},\"dateRegistered\": {},\"firstDepositDate\": {} },\"client\": {\"email\": {\"flag\": \"like\", \"value\": \"" + user_email + "\"}},\"flags\": {\"withTestUsers\": true}}"
        find_user_headers = {'Token-Type': "Bearer", 'Access-Token': token_id_pair[0], 'uid': token_id_pair[1],
                             'Content-Type': 'application/json; charset=UTF-8', 'client': 'user'}
        user_result = requests.request("POST", find_user_url, headers=find_user_headers, data=find_user_payload)
        query_id = re.search(r'id\":\"\d{5,6}', user_result.text)
        logging.info( query_id)
        user_id = re.findall('[0-9]+', query_id.group())[0]
        return [user_id,token_id_pair]
