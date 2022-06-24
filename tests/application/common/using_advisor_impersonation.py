# import os
# import random
# from datetime import datetime
# import allure
# import pytest
# from faker import Faker
# from pages.application.application_flow import StudentApplicationPage
# from pages.authentication.login_page import LoginPage
# from pages.user_management.manage_student_page import ManageStudentPage
# from tests.conftest import BaseTest
#
#
# @allure.suite("Application Flow")
# @allure.feature("Application")
# @allure.description("Test cases for application flow using impersonation")
# class TestNewStudentApplication(BaseTest):
#     """Test for Class Home Page"""
#
#     @pytest.fixture(autouse=True)
#     def _setup(self):
#         self.login_page_tab_instance = LoginPage(self.driver)
#         self.application_imper_student_instance = StudentApplicationPage(self.driver)
#         self.manage_student_instance = ManageStudentPage(self.driver)
#
#     fake = Faker()
#     fname = fake.first_name()
#     lname = fake.last_name()
#     number = "0771234" + str(random.randint(1111, 9999))
#     now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     email = f"stu.dent{now}@ischoolconnect.com"
#     stud_number = "0987654" + str(random.randint(1111, 9999))
#     identifier = fake.word()
#
#     @allure.title("Go to login page")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_00_visit_login_page(self):
#         link = os.getenv("LOGIN_LINK")
#         print(link)
#         self.login_page_tab_instance.visit_actual_page(link)
#
#     @allure.title("Validate advisor url is correct")
#     @allure.severity(allure.severity_level.MINOR)
#     def test_01_url_displayed_properly(self):
#         assert self.login_page_tab_instance.get_current_url()
#
#     @allure.title("Validate page title is correct")
#     @allure.severity(allure.severity_level.MINOR)
#     def test_02_title_displayed_properly(self):
#         self.login_page_tab_instance = LoginPage(self.driver)
#         assert self.login_page_tab_instance.check_title_text_display()
#
#     @allure.title("Click on sign with correct email id, password should reflect to student dashboard")
#     @allure.severity(allure.severity_level.CRITICAL)
#     def test_03_enter_correct_credentials(self):
#         email = os.environ.get("AUTOMATION_ADVISOR_LOGIN")
#         password = os.environ.get("AUTOMATION_ADVISOR_PASSWORD")
#         assert self.login_page_tab_instance.sign_in(email, password)
#
#     @allure.title("Validate students management screen url is correct")
#     @allure.severity(allure.severity_level.CRITICAL)
#     def test_04_check_manage_student_url(self):
#         assert self.login_page_tab_instance.check_dashboard_url(
#             os.getenv("MANAGE_USER_BASE_URL") + "manage-students"
#         )
#
#     @allure.title("Clicking on close button should close the cookies consent")
#     @allure.severity(allure.severity_level.MINOR)
#     def test_05_close_cookies_consent(self):
#         assert self.login_page_tab_instance.close_cookies_model()
#
#     @allure.title(
#         "Clicking on add student button should open student form. "
#         "Fill all the details and click on the create should create new student"
#     )
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_06_create_student(self):
#         assert self.manage_student_instance.create_student_without_advisor(
#             self.fname, self.lname, self.email, self.stud_number, self.identifier
#         )
#
#     @allure.title("Search newly created student using email id should show student below and"
#                   "Validate newly created student using student credentials")
#     @allure.severity(allure.severity_level.MINOR)
#     def test_07_search_for_newly_added_student_and_validate(self):
#         assert self.manage_student_instance.search_for_student(self.email)
#         assert self.manage_student_instance.check_for_student_name(self.fname, self.lname)
#         assert self.manage_student_instance.check_for_student_email(self.email)
#         assert self.manage_student_instance.check_for_student_number(self.stud_number)
#
#     @allure.title("Click on the action button should option actions modal and "
#                   "Click on impersonation button should open impersonation modal")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_08_click_on_action_button_to_impersonate_student(self):
#         assert self.manage_student_instance.click_on_action_button()
#         assert self.manage_student_instance.click_on_impersonate_button()
#         assert self.manage_student_instance.ok_button_impersonate_model()
#
#     @allure.title("Validate student dashboard screen url is correct as well as "
#                   "Student preference form should be appear")
#     @allure.severity(allure.severity_level.CRITICAL)
#     def test_09_check_division_dashboard_url(self):
#         assert self.login_page_tab_instance.check_dashboard_url(
#             os.getenv("STUDENT_DASHBOARD_BASE_URL")
#         )
#
#     @allure.title("Clicking on close button should close the cookies consent")
#     @allure.severity(allure.severity_level.MINOR)
#     def test_10_close_cookies_consent(self):
#         assert self.login_page_tab_instance.close_cookies_model()
#
#     @allure.title("Fill all the details present in preference form")
#     @allure.severity(allure.severity_level.CRITICAL)
#     def test_11_student_preference_form(self):
#         assert self.application_imper_student_instance.click_on_degree_to_pursue()
#         assert self.application_imper_student_instance.click_on_discipline()
#         assert self.application_imper_student_instance.click_on_year()
#         assert self.application_imper_student_instance.click_on_season()
#         assert self.application_imper_student_instance.click_on_done()
#
#     @allure.title("Clicking on explore school redirect user to explore school page")
#     @allure.severity(allure.severity_level.CRITICAL)
#     def test_12_explore_school_section(self):
#         assert self.application_imper_student_instance.click_on_student_explore_school()
#
#     @allure.title("Clicking on add to favorite and apply should added course to "
#                   "favorite list application gets applied")
#     @allure.severity(allure.severity_level.CRITICAL)
#     def test_13_click_on_add_to_favorites_and_apply_and_validate_the_same(self):
#         assert self.application_imper_student_instance.click_add_to_favorites_and_apply()
#         assert self.application_imper_student_instance.verify_added_to_favorites_and_applied()
#
#     @allure.title("Clicking on dashboard should redirect to dashboard page")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_14_dashboard_section(self):
#         assert self.application_imper_student_instance.click_on_dashboard_button()
#
#     @allure.title("Validate application status and it should be in documentation")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_15_verify_application_status_at_student_side(self):
#         assert self.application_imper_student_instance.application_status_student_side("Documentation ")
#
#     @allure.title("Clicking on form builder radio button should get selected")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_16_click_and_verify_form_builder_check_box(self):
#         assert self.application_imper_student_instance.click_on_form_builder_radio_button()
#         assert self.application_imper_student_instance.verify_form_builder_radio_button()
#
#     @allure.title("Clicking on upload document should open application document modal")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_17_click_on_upload_document(self):
#         assert self.application_imper_student_instance.click_on_upload_document()
#
#     @allure.title("Clicking passport document from drop down should get uploaded")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_18_upload_passport_document(self):
#         assert self.application_imper_student_instance.select_passport_document_type("Passport")
#         assert self.application_imper_student_instance.choose_passport1_document()
#         assert self.application_imper_student_instance.click_on_upload_button()
#
#     @allure.title("Clicking on school transcript document from drop down should get uploaded")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_19_upload_school_transcript_document(self):
#         assert self.application_imper_student_instance.select_school_transcript_document_type("Transcripts")
#         assert self.application_imper_student_instance.choose_school_transcript_document()
#         assert self.application_imper_student_instance.click_on_upload_button()
#
#     @allure.title("Clicking on university transcript document from drop down should get uploaded")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_20_upload_university_transcript_document(self):
#         assert self.application_imper_student_instance.select_university_transcript_document_type("University")
#         assert self.application_imper_student_instance.choose_university_transcript_document()
#         assert self.application_imper_student_instance.click_on_upload_button()
#
#     @allure.title("Clicking on close button should close the application documents modal")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_21_close_upload_document_modal(self):
#         assert self.application_imper_student_instance.close_upload_doc_window()
#
#     @allure.title("Clicking on upload documents radio button should get selected")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_22_upload_university_transcript_document(self):
#         assert self.application_imper_student_instance.click_on_upload_documents_radio_button()
#         assert self.application_imper_student_instance.verify_upload_documents_radio_button()
#
#     @allure.title("Clicking on sop and essay radio button should get selected")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_23_click_and_verify_sop_and_essay_at_student_side(self):
#         assert self.application_imper_student_instance.click_on_sop_essay_radio_button()
#         assert self.application_imper_student_instance.verify_sop_essay_radio_button()
#
#     @allure.title("Clicking on payment radio button should get selected")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_24_click_and_verify_payment_student_side(self):
#         assert self.application_imper_student_instance.click_on_payment_radio_button()
#         assert self.application_imper_student_instance.verify_payment_radio_button()
#
#     @allure.title("Clicking on send for review button should change the status to Under Review")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_25_click_and_verify_send_for_review_at_student_side(self):
#         assert self.application_imper_student_instance.verify_send_for_review_text("Send for Review")
#         assert self.application_imper_student_instance.click_on_send_for_review_button()
#
#     @allure.title("Validating changed status to Under Review ")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_26_verify_application_status_student_side(self):
#         assert self.application_imper_student_instance.application_status_student_side("Under Review ")
#
#     @allure.title("Click on return to impersonation should redirect to advisor dashboard")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_27_check_return_to_impersonate(self):
#         assert self.application_imper_student_instance.click_on_return_to_impersonate_button()
#
#     @allure.title("Search student by name at advisor side should show appropriate student")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_28_search_for_the_student(self):
#         assert self.application_imper_student_instance.click_on_student_application_form()
#         assert self.application_imper_student_instance.search_for_student(self.fname + " " + self.lname)
#
#     @allure.title("Search student using name at advisor side should show appropriate student")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_29_verify_application_status_at_advisor_side(self):
#         assert self.application_imper_student_instance.application_status_advisor_side("Under Review ")
#
#     @allure.title("Clicking on change status option should open change status modal")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_30_click_on_change_status_option(self):
#         assert self.manage_student_instance.click_on_action_button()
#         assert self.application_imper_student_instance.click_on_change_status_option()
#
#     @allure.title("Clicking on hold button should change the status to on hold form under review")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_31_change_status_to_on_hold(self):
#         assert self.application_imper_student_instance.change_status_to_on_hold()
#
#     @allure.title("Validating changed status to on hold")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_32_verify_application_status_at_advisor_side(self):
#         assert self.application_imper_student_instance.application_status_advisor_side("On-Hold ")
#
#     @allure.title("Clicking on change status option should open change status modal")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_33_click_on_change_status_option(self):
#         assert self.manage_student_instance.click_on_action_button()
#         assert self.application_imper_student_instance.click_on_change_status_option()
#
#     @allure.title("Clicking on under review button should change the status to under review from on hold")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_34_change_status_to_under_review(self):
#         assert self.application_imper_student_instance.change_status_to_under_review()
#
#     @allure.title("Clicking on change status option should open change status modal")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_35_click_on_change_status_option(self):
#         assert self.manage_student_instance.click_on_action_button()
#         assert self.application_imper_student_instance.click_on_change_status_option()
#
#     @allure.title("Clicking on review passed button should change the status to review passed from under review")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_36_change_status_to_review_passed(self):
#         assert self.application_imper_student_instance.change_status_to_review_passed()
#
#     @allure.title("Validate changed status to on Review Passed")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_37_verify_application_status_at_advisor_side(self):
#         assert self.application_imper_student_instance.application_status_advisor_side("Review Passed ")
#
#     @allure.title("Validating Review Passed ticket text")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_38_verify_ticket_text(self):
#         assert self.application_imper_student_instance.check_review_passed_ticket_text()
#
#     @allure.title("Clicking on change status option should open change status modal")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_39_click_on_change_status_option(self):
#         assert self.manage_student_instance.click_on_action_button()
#         assert self.application_imper_student_instance.click_on_change_status_option()
#
#     @allure.title("Clicking on awaiting_result button should change the status to awaiting result from review passed")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_40_change_status_to_awaiting_results(self):
#         assert self.application_imper_student_instance.change_status_to_awaiting_result()
#
#     @allure.title("Validate changed status to on Awaiting Results")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_41_verify_application_status_at_advisor_side(self):
#         assert self.application_imper_student_instance.application_status_advisor_side("Awaiting Results ")
#
#     @allure.title("Validating Awaiting Results ticket text")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_42_verify_ticket_text(self):
#         assert self.application_imper_student_instance.check_awaiting_result_ticket_text()
#
#     @allure.title("Clicking on change status option should open change status modal")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_43_click_on_change_status_option(self):
#         assert self.manage_student_instance.click_on_action_button()
#         assert self.application_imper_student_instance.click_on_change_status_option()
#
#     @allure.title("Clicking on conditional acceptance button should change the status to conditional acceptance "
#                   "from awaiting results")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_44_change_status_to_conditional_acceptance(self):
#         assert self.application_imper_student_instance.change_status_to_conditional_acceptance()
#
#     @allure.title("Validate changed status to Conditional Acceptance")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_45_verify_application_status_at_advisor_side(self):
#         assert self.application_imper_student_instance.application_status_advisor_side("Conditional Acceptance ")
#
#     @allure.title("Clicking on change status option should open change status modal")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_46_click_on_change_status_option(self):
#         assert self.manage_student_instance.click_on_action_button()
#         assert self.application_imper_student_instance.click_on_change_status_option()
#
#     @allure.title("Clicking on additional screening button should change the status to additional screening "
#                   "from conditional acceptance")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_47_change_status_to_additional_screening(self):
#         assert self.application_imper_student_instance.change_status_to_additional_screening()
#
#     @allure.title("Validate changed status to Additional Screening")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_48_verify_application_status_at_advisor_side(self):
#         assert self.application_imper_student_instance.application_status_advisor_side("Additional Screening ")
#
#     @allure.title("Clicking on change status option should open change status modal")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_49_click_on_change_status_option(self):
#         assert self.manage_student_instance.click_on_action_button()
#         assert self.application_imper_student_instance.click_on_change_status_option()
#
#     @allure.title("Clicking on university accepted button should change the status to university accepted "
#                   "from additional screening")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_50_change_status_to_university_accepted(self):
#         assert self.application_imper_student_instance.change_status_to_university_accepted()
#
#     @allure.title("Validate changed status to University Accepted")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_51_verify_application_status_at_advisor_side(self):
#         assert self.application_imper_student_instance.application_status_advisor_side("University Accepted ")
#
#     @allure.title("Impersonating the student to validate status")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_52_impersonate_the_student(self):
#         assert self.application_imper_student_instance.click_on_action_button_manage_application()
#         assert self.application_imper_student_instance.click_on_impersonate_button_university_accepted()
#
#     @allure.title("Clicking on Yes button present on university accepted status should accept the university")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_53_click_on_university_accepted_yes_button(self):
#         assert self.application_imper_student_instance.click_on_university_accepted_yes_button()
#
#     @allure.title("Validate change status to Admit Accepted at student side")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_54_verify_admit_accepted_status_at_student_side(self):
#         assert self.application_imper_student_instance.application_status_student_side("Admit Accepted ")
#
#     @allure.title("Click on return to impersonation should redirect to advisor dashboard")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_55_check_return_to_impersonate(self):
#         assert self.application_imper_student_instance.click_on_return_to_impersonate_button()
#
#     @allure.title("Search student by name at advisor side should show appropriate student")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_56_search_for_the_student(self):
#         assert self.application_imper_student_instance.click_on_student_application_form()
#         assert self.application_imper_student_instance.search_for_student(self.fname + " " + self.lname)
#
#     @allure.title("Clicking on change status option should open change status modal")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_57_click_on_change_status_option(self):
#         assert self.manage_student_instance.click_on_action_button()
#         assert self.application_imper_student_instance.click_on_change_status_option()
#
#     @allure.title("Clicking on financial documentation button should change the status to financial_documentation "
#                   "from admit accepted")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_58_change_status_to_conditional_acceptance(self):
#         assert self.application_imper_student_instance.change_status_to_financial_documentation()
#
#     @allure.title("Validate changed status to Financial Documentation")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_59_verify_application_status_at_advisor_side(self):
#         assert self.advisor_application.application_status_advisor_side("Financial Documentation ")
#
#     @allure.title("Clicking on change status option should open change status modal")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_60_click_on_change_status_option(self):
#         assert self.manage_student_instance.click_on_action_button()
#         assert self.application_imper_student_instance.click_on_change_status_option()
#
#     @allure.title("Clicking on final acceptance button should change the status to final acceptance "
#                   "from financial documentation")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_61_change_status_to_final_acceptance(self):
#         assert self.application_imper_student_instance.change_status_final_acceptance()
#
#     @allure.title("Validate changed status to Final Acceptance")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_62_verify_application_status_at_advisor_side(self):
#         assert self.application_imper_student_instance.application_status_advisor_side("Final Acceptance ")
#
#     @allure.title("Impersonating the student to validate status")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_63_impersonate_the_student(self):
#         assert self.application_imper_student_instance.click_on_action_button_manage_application()
#         assert self.application_imper_student_instance.click_on_impersonate_button_university_accepted()
#
#     @allure.title("Validate changed status to Final Acceptance")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_64_verify_final_acceptance_status_at_student_side(self):
#         assert self.student_application.application_status_student_side("Final Acceptance ")
#
#     @allure.title("Clicking on sign out button should redirected to login page")
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_65_sign_out(self):
#         assert self.login_page_tab_instance.student_sign_out()
