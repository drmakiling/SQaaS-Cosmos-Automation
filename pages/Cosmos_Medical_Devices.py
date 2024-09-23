import time

from playwright.sync_api import Page, expect
from utils.wait_helpers import wait_and_click_element, wait_for_element

class Medical_Devices():
    def __init__(self, page):
        self.page = page
        # Modal Buttons
        self.add_medical_device_save_button = "//button[contains(text(),'Save')]"
        self.add_medical_device_close_button = "//button[contains(text(),'Close')]"
        self.add_medical_device_cancel_button = "//button[contains(text(),'Cancel')]"
        self.back_arrow = "//*[name()='path' and @id='icon/navigation/Back']"
        self.medical_devices_tab = "//p[text()='Medical devices']"

        # Add medical device
        self.add_a_medical_device_button = "(//button[contains(text(), 'Add a medical device')])[1]"

        # GENERAL SETTINGS TAB
        self.observation_category_dropdown = "(//input[contains(@placeholder,'E.g. Blood Pressure')]/..//button)[1]"
        self.blood_pressure = "(//input[contains(@placeholder,'E.g. Blood Pressure')]/..//button)[1]/../../input"
        self.context_category_dropdown = "//input[contains(@placeholder,'E.g. PEF (Compex)')]/..//button"
        self.context_category_text_box = "(//input[contains(@placeholder,'E.g. PEF (Compex)')]/..//button)[1]/../../input"
        self.device_models_dropdown = "//input[contains(@placeholder,'E.g. Omron')]/..//button"
        self.available_devices_text_box = "//input[contains(@placeholder,'E.g. 4')]"
        self.record_description_text_box = "//textarea[contains(@placeholder,'E.g. Evening PEF with Spirobank Smart and End Action=RANDOMIZATION')]/.."

        # DEVICE SPECIFIC SETTINGS & TIMEOUTS TAB
        self.device_specific_settings_and_timeout_tab = "//button[contains(@id,'DeviceSpecificSettingsAndTimeouts-1')]"
        self.turbine_type_not_available_radio_button = "//h6[contains(text(),'Turbine type')]/..//input[contains(@value, 'N/A')]"
        self.pairing_and_discovery_timeouts_text_box = "//h6[contains(text(),'Pairing and discovery timeouts')]/..//input[contains(@name, 'DeviceSpecificSettingsAndTimeoutsSection-pairingAndDiscoveryTimeouts')]"
        self.remove_sensor_timeout_not_available_radio_button = "//h6[contains(text(),'Remove sensor timeout')]/..//input[contains(@value, 'N/A')]"
        self.threshold_of_streamed_data_duration_not_available_radio_button = "//h6[contains(text(),'Threshold of streamed data duration')]/..//input[contains(@value, 'N/A')]"
        self.time_to_take_a_measurement_text_box = "//input[@name='DeviceSpecificSettingsAndTimeoutsSection-timeToTakeAMeasurement']"
        self.ecg_measurement_minimum_duration_timeout_not_available_radio_button = "//h6[contains(text(),'ECG measurement minimum duration timeout')]/..//input[contains(@value, 'N/A')]"
        self.connection_data_timeout_not_available_radio_button = "//h6[contains(text(),'Connection data timeout')]/..//input[contains(@value, 'N/A')]"
        self.measurement_fail_timeout_text_box = "//input[@name='DeviceSpecificSettingsAndTimeoutsSection-measurementFailTimeout']"

        # Over-reader integration tab
        self.over_reader_integration_tab = "//button[contains(@id,'OverReaderIntegration-2')]"
        self.enable_integration_for_the_study_yes_radio_button = "//input[@name='OverReaderIntegrationSection-enableIntegrationForTheStudy' and @value='Yes']"
        self.enable_integration_for_the_study_no_radio_button = "//input[@name='OverReaderIntegrationSection-enableIntegrationForTheStudy' and @value='No']"

        # MEDICAL DEVICE EVENT DETECTION TAB
        self.medical_device_event_detection_tab = "//button[contains(@id,'EventDetection-3')]"
        self.algorithm_code_not_available_radio_button = "//input[@name='EventDetectionForMedicalDeviceSection-algorithmCode-field1' and @value='N/A']"
        self.threshold_text_box = "//input[@name='AlgorithmPayloadPropertiesSection-threshold']"
        self.unit_dropdown = "//div[@data-testid='AlgorithmPayloadPropertiesSection-unit']"
        self.unit_dropdown_kg = "//li[@data-value='Kg']"
        self.daysback_text_box = "//input[@name='AlgorithmPayloadPropertiesSection-daysBack']"
        self.run_in_days_text_box = "//input[@name='AlgorithmPayloadPropertiesSection-runInDays']"
        self.consecutive_events_text_box = "//input[@name='AlgorithmPayloadPropertiesSection-consecutiveEvents']"
        self.consecutive_days_text_box = "//input[@name='AlgorithmPayloadPropertiesSection-consecutiveDays']"
        self.app_unify_app_rpm_category_text_box = "//input[@name='AlgorithmPayloadPropertiesSection-AppUnifyAppRPMEventFeedbackNoticeCategory']"
        self.app_unify_app_rpm_header_text_box = "//textarea[@name='AlgorithmPayloadPropertiesSection-AppUnifyAppRPMEventFeedbackNoticeHeader']"
        self.app_unify_app_rpm_body_text_box = "//textarea[@name='AlgorithmPayloadPropertiesSection-AppUnifyAppRPMEventFeedbackNoticeBody']"
        self.web_example_text_text_box = "//input[@name='AlgorithmPayloadPropertiesSection-WebExampleTextForThresholdEventInformationForChosenAlgorithm']"
        # Device Table
        self.medical_device_three_dots = "//div[@role='cell']//button[@type='button']//*[name()='svg']"
        self.three_dot_view = "//ul[@role='menu']//span[contains(text(),'View')]"
        self.three_dot_delete = "//ul[@role='menu']//span[contains(text(),'Delete')]"

        # App Settings Tab
        self.app_settings_tab = "//button[contains(text(), 'App settings')]"

        # General Settings Edit Button
        self.general_settings_edit_button = "//div[contains(@data-testid,'app-settings-general-settings-card')]//button[contains(@class,'MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways MuiLink-button css-95lpad')][normalize-space()='Edit']"

        # Pin Entry
        self.pin_entry_second_auth_yes_radio_button = "//input[@name='GeneralSettingsSection-secondAuthenticationRequired' and @value='Yes']"
        self.pin_entry_second_auth_no_radio_button = "//input[@name='GeneralSettingsSection-secondAuthenticationRequired' and @value='No']"

        # Data Retention Time
        self.data_retention_time_text_box = "//input[@name='GeneralSettingsSection-dataRetentionTime']"

        # Number of Minimum Observations
        self.num_min_observation_dropdown = "//input[@placeholder='E.g. 3']/../div"
        self.num_min_observation_dropdown_choice = "//li[@data-value='3']"

        # Number of Maximum Observations
        self.num_max_observation_dropdown = "//input[@placeholder='E.g. 4']/../div"
        self.num_max_observation_dropdown_choice = "//li[@data-value='4']"

        # Enable Scheduled Tasks
        self.enable_schedule_tasks_yes_radio_button = "//input[@name='GeneralSettingsSection-enableScheduledTasks' and @value='Yes']"
        self.enable_schedule_tasks_no_radio_button = "//input[@name='GeneralSettingsSection-enableScheduledTasks' and @value='No']"

        # Enable Manual Measurements
        self.enable_manual_measurement_yes_radio_button = "//input[@name='GeneralSettingsSection-enableManualMeasurements' and @value='Yes']"
        self.enable_manual_measurement_no_radio_button = "//input[@name='GeneralSettingsSection-enableManualMeasurements' and @value='No']"

        # Source of Observation Timestamp
        self.source_of_observation_dropdown = "//input[@placeholder='E.g. Sensor']/../div"
        self.source_of_observation_dropdown_sensor_choice = "//li[@data-value='Sensor']"
        self.source_of_observation_dropdown_phone_choice = "//li[@data-value='Phone']"

        # Display Measurement Observations to Patient
        self.display_measurement_dropdown = "//input[@placeholder='E.g. Visible']/../div"
        self.display_measurement_dropdown_choice_visible = "//li[@data-value='Visible']"
        self.display_measurement_dropdown_choice_hidden = "//li[@data-value='Hidden']"

        # Device Specific Settings Tab
        self.device_specific_settings_edit_button = "//div[contains(@data-testid,'app-settings-device-specific-settings-card')]//button[contains(@class,'MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways MuiLink-button css-95lpad')][normalize-space()='Edit']"
        self.device_specific_settings_tab = "//button[@id='DeviceSpecificSettings-1']"

        # Insert Temperature
        self.insert_temp_not_available_radio_button = "//input[@name='DeviceSpecificSettingsSection-insertTemperature-field1' and @value='Not available']"
        self.insert_temp_select_option_radio_button = "//input[@name='DeviceSpecificSettingsSection-insertTemperature-field1' and @value='Select option']"

        # Include Training Video
        self.include_training_video_not_available_radio_button = "//input[@name='DeviceSpecificSettingsSection-includeTrainingVideo-field1' and @value='Not available']"
        self.include_training_video_select_option_radio_button = "//input[@name='DeviceSpecificSettingsSection-includeTrainingVideo-field1' and @value='Select option']"

        # Web Portal Tab
        self.web_portal_tab = "//button[contains(text(), 'Web portal')]"
        self.web_portal_general_settings_edit_button = "//button[normalize-space()='Edit']"

        # Source of Last Sync
        self.source_of_last_sync_dropdown = "//input[@placeholder='E.g. Observation']/../div"
        self.source_of_last_sync_dropdown_heartbeat = "//li[@data-value='Heartbeat']"
        self.source_of_last_sync_dropdown_observation = "//li[@data-value='Observation']"

        # Show Session Details Page
        self.show_session_details_page_yes_radio_button = "//input[@name='GeneralSettingsSection-showSessionDetailsPage' and @value='Yes']"
        self.show_session_details_page_no_radio_button = "//input[@name='GeneralSettingsSection-showSessionDetailsPage' and @value='No']"

        # Enable CTA to Power BI
        self.enable_cta_to_power_bi_yes_radio_button = "//input[@name='GeneralSettingsSection-enableCTAtoPowerBI' and @value='Yes']"
        self.enable_cta_to_power_bi_no_radio_button = "//input[@name='GeneralSettingsSection-enableCTAtoPowerBI' and @value='No']"
        # Compliance Tab
        self.Complaince_tab = "//button[contains(text(), 'Compliance')]"
        self.Compliance_General_settings_edit_button = "//div[@data-testid='compliance-general-settings-card']//button[@class='MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways MuiLink-button css-95lpad'][normalize-space()='Edit']"
        self.Compliance_Content_edit_button = "//div[@data-testid='compliance-content-card']//button[@class='MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways MuiLink-button css-95lpad'][normalize-space()='Edit']"
        # Edit Compliance
        self.Compliance_Yes_radio_button = "//input[@name='GeneralSettingsSection-compliance' and @value='Yes']"
        self.Compliance_No_radio_button = "//input[@name='GeneralSettingsSection-compliance' and @value='No']"
        # Threshold
        self.Threshold_Not_Availible_radio_button = "//input[@name='GeneralSettingsSection-threshold-field1' and @value='N/A']"
        self.Threshold_Enter_Percentage_radio_button = "//input[@name='GeneralSettingsSection-threshold-field1' and @value='Enter percentage']"

        # Content Tab
        self.Edit_Compliance_Content_tab = "//button[@id='Content-1']"
        # Compliance calculation title
        self.Compliance_Calc_title_Not_avaliable_radio_button = "//input[@name='ContentSection-complianceCalculationTitle-field1' and @value='N/A']"
        self.Compliance_Calc_title_Enter_title_radio_button = "//input[@name='ContentSection-complianceCalculationTitle-field1' and @value='Enter title']"
        # Compliance calculation body
        self.Compliance_Calc_body_Not_avaliable_radio_button = "//input[@name='ContentSection-complianceCalculationBody-field1' and @value='N/A']"
        self.Compliance_Calc_body_Enter_body_radio_button = "//input[@name='ContentSection-complianceCalculationBody-field1' and @value='Enter body']"
        # Compliance rate title
        self.Compliance_rate_title_Not_avaliable_radio_button = "//input[@name='ContentSection-complianceRateTitle-field1' and @value='N/A']"
        self.Compliance_rate_title_Enter_title_radio_button = "//input[@name='ContentSection-complianceRateTitle-field1' and @value='Enter title']"
        # Compliance rate body
        self.Compliance_rate_body_Not_avaliable_radio_button = "//input[@name='ContentSection-complianceRateBody-field1' and @value='N/A']"
        self.Compliance_rate_body_Enter_body_radio_button = "//input[@name='ContentSection-complianceRateBody-field1' and @value='Enter body']"
        # Threshold title
        self.Threshold_title_Not_avaliable_radio_button = "//input[@name='ContentSection-thresholdTitle-field1' and @value='N/A']"
        self.Threshold_Calc_title_Enter_title_radio_button = "//input[@name='ContentSection-thresholdTitle-field1' and @value='Enter title']"
        # Threshold body
        self.Threshold_body_Not_avaliable_radio_button = "//input[@name='ContentSection-thresholdBody-field1' and @value='N/A']"
        self.Threshold_body_Enter_body_radio_button = "//input[@name='ContentSection-thresholdBody-field1' and @value='Enter body']"

        # Patient Schedule Tab
        self.Patient_Schedule_tab = "//button[contains(text(), 'Patient schedule')]"
        # Configuration Manager settings
        self.Configuration_manager_settings_edit_button = "//div[@data-testid='medical-devices-configuration-manager-settings-card']//button[@class='MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways MuiLink-button css-95lpad'][normalize-space()='Edit']"
        self.Schedule_code_text_box = "//input[@name='ConfigurationManagerSettingsSection-scheduleCode']"
        self.Version_code_for_schedule_text_box = "//input[@name='ConfigurationManagerSettingsSection-versionCodeForSchedule']"
        self.Request_code_text_box = "//input[@name='ConfigurationManagerSettingsSection-requestCode']"
        self.Device_Schedule_group_text_Box = "//input[@name='ConfigurationManagerSettingsSection-devicesScheduleGroup']"
        self.PTCMS_Order_textbox = "//input[@name='ConfigurationManagerSettingsSection-order']"
        # Medical Devices Availability of Activities
        self.Medical_devices_availability_of_activities_tab = "//button[@id='AvailabilityOfActivities-1']"
        self.availability_of_activities_Enable_schedule_tasks_Yes_radio_button = "//input[@name='AvailabilityOfActivitiesSection-enableScheduledTasks' and @value='Yes']"
        self.availability_of_activities_Enable_schedule_tasks_No_radio_button = "//input[@name='AvailabilityOfActivitiesSection-enableScheduledTasks' and @value='No']"
        self.Activation_Window_start_text_box = "//h6[contains(text(),'Activation window start')]//..//input"
        self.Activation_Window_end_text_box = "//h6[contains(text(),'Activation window end')]//..//input"
        self.Start_action_dropdown = "//h6[contains(text(),'Start action')]//..//input[@role='combobox']"
        self.Start_action_dropdown_Screening = "//li[@data-value='SCREENING']"
        self.Start_action_dropdown_Randomization = "//li[@data-value='RANDOMIZATION']"
        self.Start_action_dropdown_Activation = "//li[@data-value='ACTIVATION']"
        self.Start_action_specific_time_point_na_radio_button = "//input[@name='AvailabilityOfActivitiesSection-startActionSpecificTimePoint-field1' and @value='N/A']"
        self.Start_action_specific_time_point_enter_time_radio_button = "//input[@name='AvailabilityOfActivitiesSection-startActionSpecificTimePoint-field1' and @value='Enter time']"
        self.Start_action_offset_na_radio_button = "//input[@name='AvailabilityOfActivitiesSection-startActionOffset-field1' and @value='N/A']"
        self.Start_action_offset_specify_offset_radio_button = "//input[@name='AvailabilityOfActivitiesSection-startActionOffset-field1' and @value='Specify offset']"
        self.End_action_na_radio_button = "//input[@name='AvailabilityOfActivitiesSection-endAction-field1' and @value='N/A']"
        self.End_action_select_status_button = "//input[@name='AvailabilityOfActivitiesSection-endAction-field1' and @value='Select status']"
        self.End_action_specific_time_point_na_radio_button = "//input[@name='AvailabilityOfActivitiesSection-endActionSpecificTimePoint-field1' and @value='N/A']"
        self.End_action_specific_time_point_select_time_button = "//input[@name='AvailabilityOfActivitiesSection-endActionSpecificTimePoint-field1' and @value='Specify time']"
        self.End_action_offset_na_radio_button = "//input[@name='AvailabilityOfActivitiesSection-endActionOffset-field1' and @value='N/A']"
        self.End_action_offset_specify_offset_radio_button = "//input[@name='AvailabilityOfActivitiesSection-endActionOffset-field1' and @value='Specify offset']"
        self.Window_before_na_radio_button = "//input[@name='AvailabilityOfActivitiesSection-windowBefore-field1' and @value='N/A']"
        self.Window_before_specify_window_radio_button = "//input[@name='AvailabilityOfActivitiesSection-windowBefore-field1' and @value='Specify window']"
        self.Window_after_na_radio_button = "//input[@name='AvailabilityOfActivitiesSection-windowAfter-field1' and @value='N/A']"
        self.Window_after_specify_window_radio_button = "//input[@name='AvailabilityOfActivitiesSection-windowAfter-field1' and @value='Specify window']"
        self.Period_na_radio_button = "//input[@name='AvailabilityOfActivitiesSection-period-field1' and @value='N/A']"
        self.Period_specify_period_radio_button = "//input[@name='AvailabilityOfActivitiesSection-period-field1' and @value='Specify period']"
        self.Frequency_na_radio_button = "//input[@name='AvailabilityOfActivitiesSection-frequency-field1' and @value='N/A']"
        self.Frequency_specify_frequency_radio_button = "//input[@name='AvailabilityOfActivitiesSection-frequency-field1' and @value='Specify frequency']"
        self.Max_Frequency_na_radio_button = "//input[@name='AvailabilityOfActivitiesSection-maxFrequency-field1' and @value='N/A']"
        self.Max_Frequency_specify_max_frequency_radio_button = "//input[@name='AvailabilityOfActivitiesSection-maxFrequency-field1' and @value='Specify max frequency']"
        self.Day_of_week_na_radio_button = "//input[@name='AvailabilityOfActivitiesSection-dayOfWeek-field1' and @value='Not available']"
        self.Day_of_week_specify_days_radio_button = "//input[@name='AvailabilityOfActivitiesSection-dayOfWeek-field1' and @value='Specify days']"
        self.Time_of_day_na_radio_button = "//input[@name='AvailabilityOfActivitiesSection-timeOfDay-field1' and @value='N/A']"
        self.Time_of_day_specify_input_radio_button = "//input[@name='AvailabilityOfActivitiesSection-timeOfDay-field1' and @value='Time input']"

        # On-demand Activity Schedule
        self.On_demand_activity_schedule_tab = "//button[@id='OnDemandActivitySchedule-2']"
        self.Remote_initiated_na_radio_button = "//input[@name='OnDemandActivityScheduleSection-remoteInitiated-field1' and @value='Not available']"
        self.Remote_initiated_text_input_radio_button = ""  # Locator missing
        self.Activity_period_na_radio_button = "//input[@name='OnDemandActivityScheduleSection-activityPeriod-field1' and @value='Not available']"
        self.Activity_period_text_input_radio_button = ""  # Locator missing
        self.Activity_duration_na_radio_button = "//input[@name='OnDemandActivityScheduleSection-activityDuration-field1' and @value='Not available']"
        self.Activity_duration_numerical_input_radio_button = ""  # Locator missing
        self.Enable_on_demand_activities_dropdown = "//h6[contains(text(),'Enable on-demand activities')]//..//div[@role='button']"
        self.Enable_on_demand_activities_dropdown_not_available = "//li[@data-value='Not available']"
        self.Enable_on_demand_activities_dropdown_Yes = ""  # Locator missing
        self.Enable_on_demand_activities_dropdown_No = ""  # Locator missing
        self.Track_on_demand_missed_session_dropdown = "//h6[contains(text(),'Track on-demand missed sessions')]//..//div[@role='button']"
        self.Track_on_demand_missed_session_dropdown_not_available = "//li[@data-value='Not available']"
        self.Track_on_demand_missed_session_dropdown_Yes = ""  # Locator missing
        self.Track_on_demand_missed_session_dropdown_No = ""  # Locator missing

        # Level of Organisation
        self.Level_of_organisation_tab = "//button[@id='LevelOfOrganisation-3']"
        self.Scheduling_applies_to_level_of_organisation_dropdown = "//h6[contains(text(),'Scheduling applies to level of organisation')]//..//div[@role='button']"
        self.Scheduling_applies_to_level_of_organisation_dropdown_study = "//li[@data-value='Study']"
        self.Scheduling_applies_to_level_of_organisation_dropdown_country = "//li[@data-value='Country']"
        self.Scheduling_applies_to_level_of_organisation_dropdown_site = "//li[@data-value='Site']"
        self.Applicable_countries_for_schedule_all_countries_radio_button = "//input[@name='LevelOfOrganisationSection-applicableCountriesForSchedule-field1' and  @value='All countries']"
        self.Applicable_countries_for_schedule_select_countries_radio_button = "//input[@name='LevelOfOrganisationSection-applicableCountriesForSchedule-field1' and @value='Select countries']"
        self.Applicable_sites_for_schedule_all_radio_button = "//input[@name='LevelOfOrganisationSection-applicableSitesForSchedule-field1' and @value='All']"
        self.Applicable_sites_for_schedule_specify_siteid_radio_button = "//input[@name='LevelOfOrganisationSection-applicableSitesForSchedule-field1' and @value='Specify SiteID(s)']"
        # Content Tab
        self.Medical_devices_content_tab = "//button[contains(text(), 'Content')"

        # Settings
        self.Content_tab_Settings_edit_button = "//div[contains(@data-testid,'content-settings-card')]//button[contains(@class,'MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways MuiLink-button css-95lpad')][normalize-space()='Edit']"
        self.Hide_go_to_instruction_button_dropdown = "//input[@placeholder='E.g. Hide']/../div"
        self.Hide_go_to_instruction_button_dropdown_hide = "//li[@data-value='Hide']"
        self.Hide_go_to_instruction_button_dropdown_show = "//li[@data-value='Show']"

        # App Content
        self.App_content_tab = "//button[@id='AppContent-1']"

        # Template: UnifyAppSensorInstruction
        self.UASInstruction_instruction_type_na_radio_button = "//input[@name='UnifyAppSensorInstructionSection-instructionType-field1' and @value='Not available']"
        self.UASInstruction_instruction_type_specify_type_radio_button = "//input[@name='UnifyAppSensorInstructionSection-instructionType-field1' and @value='Specify type']"
        self.UASInstruction_step_number_na_radio_button = "//input[@name='UnifyAppSensorInstructionSection-stepNumber-field1' and @value='Not available']"
        self.UASInstruction_step_number_specify_number_radio_button = "//input[@name='UnifyAppSensorInstructionSection-stepNumber-field1' and @value='Specify type']"
        self.UASInstruction_Header_na_radio_button = "//input[@name='UnifyAppSensorInstructionSection-header-field1' and @value='Not available']"
        self.UASInstruction_Header_specify_header_radio_button = "//input[@name='UnifyAppSensorInstructionSection-header-field1' and @value='Specify header']"
        self.UASInstruction_Body_na_radio_button = "//input[@name='UnifyAppSensorInstructionSection-body-field1' and @value='Not available']"
        self.UASInstruction_Body_specify_body_radio_button = "//input[@name='UnifyAppSensorInstructionSection-body-field1' and @value='Specify body']"
        self.UASInstruction_Instruction_image_na_radio_button = "//input[@name='UnifyAppSensorInstructionSection-instructionImage-field1' and @value='Not available']"
        self.UASInstruction_Instruction_image_specify_file_name_radio_button = "//input[@name='UnifyAppSensorInstructionSection-instructionImage-field1' and @value='Specify file name']"
        self.UASInstruction_Video_file_na_radio_button = "//input[@name='UnifyAppSensorInstructionSection-videoFile-field1' and @value='Not available']"
        self.UASInstruction_Video_file_specify_file_name_radio_button = "//input[@name='UnifyAppSensorInstructionSection-videoFile-field1' and @value='Specify file name']"
        self.UASInstruction_Video_Cover_Image_na_radio_button = "//input[@name='UnifyAppSensorInstructionSection-videoCoverImage-field1' and @value='Not available']"
        self.UASInstruction_Video_Cover_Image_specify_file_name_radio_button = "//input[@name='UnifyAppSensorInstructionSection-videoCoverImage-field1' and @value='Specify file name']"
        self.UASInstruction_No_Internet_image_na_radio_button = "//input[@name='UnifyAppSensorInstructionSection-noInternetImage-field1' and @value='Not available']"
        self.UASInstruction_No_Internet_image_specify_file_name_radio_button = "//input[@name='UnifyAppSensorInstructionSection-noInternetImage-field1' and @value='Specify file name']"

        # Template: UnifyAppSensorIntroduction
        self.UASIntroduction_instruction_type_na_radio_button = "//input[@name='UnifyAppSensorIntroductionSection-introductionType-field1' and @value='Not available']"
        self.UASIntroduction_instruction_type_specify_type_radio_button = "//input[@name='UnifyAppSensorIntroductionSection-introductionType-field1' and @value='Specify type']"
        self.UASIntroduction_step_number_na_radio_button = "//input[@name='UnifyAppSensorIntroductionSection-stepNumber-field1' and @value='Not available']"
        self.UASIntroduction_step_number_specify_number_radio_button = "//input[@name='UnifyAppSensorIntroductionSection-stepNumber-field1' and @value='Specify type']"
        self.UASIntroduction_Header_na_radio_button = "//input[@name='UnifyAppSensorIntroductionSection-header-field1' and @value='Not available']"
        self.UASIntroduction_Header_specify_header_radio_button = "//input[@name='UnifyAppSensorIntroductionSection-header-field1' and @value='Specify header']"
        self.UASIntroduction_Body_na_radio_button = "//input[@name='UnifyAppSensorIntroductionSection-body-field1' and @value='Not available']"
        self.UASIntroduction_Body_specify_body_radio_button = "//input[@name='UnifyAppSensorIntroductionSection-body-field1' and @value='Specify body']"
        self.UASIntroduction_Instruction_image_na_radio_button = "//input[@name='UnifyAppSensorIntroductionSection-introductionImage-field1' and @value='Not available']"
        self.UASIntroduction_Instruction_image_specify_file_name_radio_button = "//input[@name='UnifyAppSensorIntroductionSection-introductionImage-field1' and @value='Specify file name']"
        self.UASIntroduction_Video_file_na_radio_button = "//input[@name='UnifyAppSensorIntroductionSection-videoFile-field1' and @value='Not available']"
        self.UASIntroduction_Video_file_specify_file_name_radio_button = "//input[@name='UnifyAppSensorIntroductionSection-videoFile-field1' and @value='Specify file name']"
        self.UASIntroduction_Video_Cover_Image_na_radio_button = "//input[@name='UnifyAppSensorIntroductionSection-videoCoverImage-field1' and @value='Not available']"
        self.UASIntroduction_Video_Cover_Image_specify_file_name_radio_button = "//input[@name='UnifyAppSensorIntroductionSection-videoCoverImage-field1' and @value='Specify file name']"
        self.UASIntroduction_No_Internet_image_na_radio_button = "//input[@name='UnifyAppSensorIntroductionSection-noInternetImage-field1' and @value='Not available']"
        self.UASIntroduction_No_Internet_image_specify_file_name_radio_button = "//input[@name='UnifyAppSensorIntroductionSection-noInternetImage-field1' and @value='Specify file name']"

        # Template: UnifyAppSensorDeviceName
        self.UASDeviceName_context_type_na_radio_button = "//input[@name='UnifyAppSensorMeasurementContext-contextType-field1' and @value='Not available']"
        self.UASDeviceName_context_type_Specify_type_radio_button = "//input[@name='UnifyAppSensorMeasurementContext-contextType-field1' and @value='Specify type']"
        self.UASDeviceName_title_intro_na_radio_button = "//input[@name='UnifyAppSensorMeasurementContext-titleIntro-field1' and @value='Not available']"
        self.UASDeviceName_title_intro_Specify_title_radio_button = "//input[@name='UnifyAppSensorMeasurementContext-titleIntro-field1' and @value='Specify title']"
        self.UASDeviceName_Description_na_radio_button = "//input[@name='UnifyAppSensorMeasurementContext-descriptionIntro-field1' and @value='Not available']"
        self.UASDeviceName_Description_Specify_description_radio_button = "//input[@name='UnifyAppSensorMeasurementContext-descriptionIntro-field1' and @value='Specify description']"
        self.UASDeviceName_Daisy_chaining_na_radio_button = "//input[@name='UnifyAppSensorMeasurementContext-daisyChainingActivities-field1' and @value='Not available']"
        self.UASDeviceName_Daisy_chaining_Specify_activities_radio_button = "//input[@name='UnifyAppSensorMeasurementContext-daisyChainingActivities-field1' and @value='Specify activities']"
        self.UASDeviceName_Template_na_radio_button = "//input[@name='UnifyAppSensorMeasurementContext-template-field1' and @value='Not available']"
        self.UASDeviceName_Template_Specify_template_radio_button = "//input[@name='UnifyAppSensorMeasurementContext-template-field1' and @value='Specify template']"
        self.UASDeviceName_Identifier_na_radio_button = "//input[@name='UnifyAppSensorMeasurementContext-identifier-field1' and @value='Not available']"
        self.UASDeviceName_Identifier_Specify_title_radio_button = "//input[@name='UnifyAppSensorMeasurementContext-identifier-field1' and @value='Specify title']"
        self.UASDeviceName_title_na_radio_button = "//input[@name='UnifyAppSensorMeasurementContext-title-field1' and @value='Not available']"
        self.UASDeviceName_title_Specify_description_radio_button = "//input[@name='UnifyAppSensorMeasurementContext-title-field1' and @value='Specify description']"
        self.UASDeviceName_Subheader_na_radio_button = "//input[@name='UnifyAppSensorMeasurementContext-subheader-field1' and @value='Not available']"
        self.UASDeviceName_Subheader_Specify_description_radio_button = "//input[@name='UnifyAppSensorMeasurementContext-subheader-field1' and @value='Specify description']"

        # Web Content
        self.Web_content_tab = "//button[@id='WebContent-2']"

        # Fill Web Content
        self.request_title_text_box = "//input[@name='WebContentSection-requestTitle']"
        self.measurment_description_text_area = "//textarea[@name='WebContentSection-measurementDescription']"
        self.Schedule_description_text_area = "//textarea[@name='WebContentSection-scheduleDescription']"
        self.Reversibility_text_box = "//textarea[@name='WebContentSection-reversibility']"
        self.Placeholder_text_box = "//textarea[@name='WebContentSection-placeHolder']"

        self.Reversibility_spirometry_na_radio_button = "//input[@name='WebContentSection-reversibilitySpirometryDetails-field1' and @value='Not available']"
        self.Reversibility_spirometry_specify_reversibility_title_radio_button = "//input[@name='WebContentSection-reversibilitySpirometryDetails-field1' and @value='Specify reversibility title']"
        self.Description_regarding_na_radio_button = "//input[@name='WebContentSection-descriptionRegardingSpirometry-field1' and @value='Not available']"
        self.Description_regarding_specify_reversibility_description_radio_button = "//input[@name='WebContentSection-descriptionRegardingSpirometry-field1' and @value='Specify reversibility description']"
        self.Info_in_learn_na_radio_button = "//input[@name='WebContentSection-informationInLearnMoreDrawerForSpirometryReversibilityResult-field1' and @value='Not available']"
        self.Info_in_learn_specify_information_radio_button = "//input[@name='WebContentSection-informationInLearnMoreDrawerForSpirometryReversibilityResult-field1' and @value='Specify information']"

    from utils.wait_helpers import wait_and_click_element, wait_for_element

    def add_medical_device(self):
        # Medical device creation
        wait_and_click_element(self.page, self.Medical_devices_tab)
        wait_and_click_element(self.page, self.Add_a_medical_device_button)

        # GENERAL SETTINGS TAB OF MODAL
        wait_and_click_element(self.page, self.Observation_Category_dropdown)
        wait_for_element(self.page, self.Blood_Pressure).fill("Blood Pressure")
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        # Fill Context category section
        wait_and_click_element(self.page, self.Context_catagory_dropdown)
        wait_for_element(self.page, self.Context_catagory_text_box).fill("N/A")
        self.page.keyboard.press("Enter")
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        # Fill Device models section
        wait_and_click_element(self.page, self.Device_Modals_dropdown)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        # Fill Available devices section
        wait_and_click_element(self.page, self.Available_devices_text_box)
        wait_for_element(self.page, self.Available_devices_text_box).fill("3")
        self.page.keyboard.press("Enter")

        # Fill Record Description
        wait_and_click_element(self.page, self.Record_description_text_box)
        wait_for_element(self.page, self.Record_description_text_box).fill("test")
        self.page.keyboard.press("Enter")

        # Click Save button
        wait_and_click_element(self.page, self.Add_medical_device_save_button)

        # DEVICE SPECIFIC SETTINGS & TIMEOUTS TAB OF MODAL
        wait_and_click_element(self.page, self.Device_specific_Settings_and_timeout_tab)

        # Turbine type
        wait_and_click_element(self.page, self.Turbine_type_Not_availible_radio_button)

        # Pairing and discovery timeouts
        wait_and_click_element(self.page, self.Pairing_and_Discovery_timeouts_text_box)
        wait_for_element(self.page, self.Pairing_and_Discovery_timeouts_text_box).fill("60")
        self.page.keyboard.press("Enter")

        # Remove sensor timeout
        wait_and_click_element(self.page, self.Remove_Sensor_Timeout_Not_Availible_radio_button)

        # Threshold of streamed data duration
        wait_and_click_element(self.page, self.Threshold_of_streamed_data_duration_Not_Availible_radio_button)

        # ECG measurement minimum duration timeout
        wait_and_click_element(self.page, self.ECG_measurement_minimum_duration_timeout_not_available_radio_button)

        # Connection data timeout
        wait_and_click_element(self.page, self.Connection_data_timeout_not_available_radio_button)

        # Click Save button
        wait_and_click_element(self.page, self.Add_medical_device_save_button)

        # OVER_READER INTEGRATION TAB MODAL
        wait_and_click_element(self.page, self.Over_reader_intergration_tab)
        wait_and_click_element(self.page, self.Enable_integration_for_the_study_No_radio_button)

        # Click Save button
        wait_and_click_element(self.page, self.Add_medical_device_save_button)

        # MEDICAL DEVICE EVENT DETECTION TAB MODAL
        wait_and_click_element(self.page, self.Medical_Device_event_detection_tab)

        # Algorithm code
        wait_and_click_element(self.page, self.Algorithm_code_not_available_radio_button)

        # Threshold
        wait_and_click_element(self.page, self.Threshold_text_box)
        wait_for_element(self.page, self.Threshold_text_box).fill("test")

        # Unit dropdown
        wait_and_click_element(self.page, self.Unit_dropdown)
        wait_and_click_element(self.page, self.Unit_dropdown_kg)

        # DaysBack
        wait_and_click_element(self.page, self.daysback_text_box)
        wait_for_element(self.page, self.daysback_text_box).fill("test")

        # RunIn Days
        wait_and_click_element(self.page, self.runIn_Days_text_box)
        wait_for_element(self.page, self.runIn_Days_text_box).fill("test")

        # ConsecutiveEvents
        wait_and_click_element(self.page, self.ConsecutiveEvents_text_box)
        wait_for_element(self.page, self.ConsecutiveEvents_text_box).fill("test")

        # ConsecutiveDays
        wait_and_click_element(self.page, self.ConsecutiveDays_text_box)
        wait_for_element(self.page, self.ConsecutiveDays_text_box).fill("test")

        # APP-Unify App RPM event feedback notice - Category
        wait_and_click_element(self.page, self.APP_Uify_App_RPM_category_text_box)
        wait_for_element(self.page, self.APP_Uify_App_RPM_category_text_box).fill("test")

        # APP-Unify App RPM event feedback notice - Header
        wait_and_click_element(self.page, self.APP_Uify_App_RPM_Header_text_box)
        wait_for_element(self.page, self.APP_Uify_App_RPM_Header_text_box).fill("test")

        # APP-Unify App RPM event feedback notice - Body
        wait_and_click_element(self.page, self.APP_Uify_App_RPM_Body_text_box)
        wait_for_element(self.page, self.APP_Uify_App_RPM_Body_text_box).fill("test")

        # WEB-Example text for "Threshold event information" for chosen algorithm
        wait_and_click_element(self.page, self.WEB_example_text_text_box)
        wait_for_element(self.page, self.WEB_example_text_text_box).fill("test")

        # Click Save button
        wait_and_click_element(self.page, self.Add_medical_device_save_button)

        # Close Modal
        wait_and_click_element(self.page, self.Add_medical_device_close_button)

    def Medical_device_App_settings(self):
        # Three dot device table
        wait_and_click_element(self.page, self.Medical_device_three_dots)
        wait_and_click_element(self.page, self.Three_dot_View)

        # App Settings
        wait_and_click_element(self.page, self.App_Settings_Tab)

        # General Settings edit button
        wait_and_click_element(self.page, self.General_settings_edit_button)

        # Pin entry
        wait_and_click_element(self.page, self.Pin_entry_Second_Auth_No_radio_button)

        # Date Retention
        wait_and_click_element(self.page, self.Data_Retention_time_text_box)
        wait_for_element(self.page, self.Data_Retention_time_text_box).fill('10')

        # Number of minimum observations
        wait_and_click_element(self.page, self.Num_Min_Observation_dropdown)
        wait_and_click_element(self.page, self.Num_Min_Observation_dropdown_choice)

        # Number of maximum observations
        wait_and_click_element(self.page, self.Num_Max_Observation_dropdown)
        wait_and_click_element(self.page, self.Num_Max_Observation_dropdown_choice)

        # Enable scheduled tasks
        wait_and_click_element(self.page, self.Enable_schedule_tasks_Yes_radio_button)

        # Enable manual measurements
        wait_and_click_element(self.page, self.Enable_Manual_Measurement_Yes_radio_button)

        # Source of observation timestamp
        wait_and_click_element(self.page, self.Source_of_observation_dropdown)
        wait_and_click_element(self.page, self.Source_of_observation_dropdown_Sensor_Choice)

        # Display measurement observations to patient
        wait_and_click_element(self.page, self.Display_Measurment_dropdown)
        wait_and_click_element(self.page, self.Display_Measurment_dropdown_Choice_Visible)

        # Click Save button
        wait_and_click_element(self.page, self.Add_medical_device_save_button)

        # Device Specific Settings tab
        wait_and_click_element(self.page, self.Device_Specific_Settings_tab)
        wait_and_click_element(self.page, self.insert_Temp_Not_Available_radio_button)
        wait_and_click_element(self.page, self.Include_Training_video_Not_Available_radio_button)

        # Click Save button
        wait_and_click_element(self.page, self.Add_medical_device_save_button)

        # Close Modal
        wait_and_click_element(self.page, self.Add_medical_device_close_button)

    # Fill out Web Portal tab
    def Medical_device_Web_portal(self):
        # Click web portal tab
        wait_and_click_element(self.page, self.Web_portal_tab)
        wait_and_click_element(self.page, self.Web_portal_General_seetings_edit_button)
        wait_and_click_element(self.page, self.Source_of_last_sync_dropdown)
        wait_and_click_element(self.page, self.Source_of_last_sync_dropdown_Observation)
        wait_and_click_element(self.page, self.Show_Session_details_page_Yes_radio_button)
        wait_and_click_element(self.page, self.Enable_CTA_to_power_BI_Yes_radio_button)

        # Click Save button
        wait_and_click_element(self.page, self.Add_medical_device_save_button)

        # Close Modal
        wait_and_click_element(self.page, self.Add_medical_device_close_button)

    # Fill out Compliance tab
    def Medical_device_Compliance(self):
        # Click compliance tab
        wait_and_click_element(self.page, self.Complaince_tab)

        # Click General settings edit button
        wait_and_click_element(self.page, self.Compliance_General_settings_edit_button)

        # Fill out general settings
        wait_and_click_element(self.page, self.Compliance_Yes_radio_button)
        wait_and_click_element(self.page, self.Threshold_Not_Availible_radio_button)

        # Click Save button
        wait_and_click_element(self.page, self.Add_medical_device_save_button)

        # Click content tab
        wait_and_click_element(self.page, self.Edit_Compliance_Content_tab)

        # Fill out content
        wait_and_click_element(self.page, self.Compliance_Calc_title_Not_avaliable_radio_button)
        wait_and_click_element(self.page, self.Compliance_Calc_body_Not_avaliable_radio_button)
        wait_and_click_element(self.page, self.Compliance_rate_title_Not_avaliable_radio_button)
        wait_and_click_element(self.page, self.Compliance_rate_body_Not_avaliable_radio_button)
        wait_and_click_element(self.page, self.Threshold_title_Not_avaliable_radio_button)
        wait_and_click_element(self.page, self.Threshold_body_Not_avaliable_radio_button)

        # Click Save button
        wait_and_click_element(self.page, self.Add_medical_device_save_button)

        # Close Modal
        wait_and_click_element(self.page, self.Add_medical_device_close_button)

    # Fill out Patient Schedule tab
    def Medical_device_patient_schedule(self):
        # Click patient schedule tab
        wait_and_click_element(self.page, self.Patient_Schedule_tab)

        # Fill out configuration manager settings
        wait_and_click_element(self.page, self.Configuration_manager_settings_edit_button)
        wait_and_click_element(self.page, self.Schedule_code_text_box)
        self.page.fill(self.Schedule_code_text_box, "test")

        wait_and_click_element(self.page, self.Version_code_for_schedule_text_box)
        self.page.fill(self.Version_code_for_schedule_text_box, "2.0")

        wait_and_click_element(self.page, self.Request_code_text_box)
        self.page.fill(self.Request_code_text_box, "test")

        wait_and_click_element(self.page, self.Device_Schedule_group_text_Box)
        self.page.fill(self.Device_Schedule_group_text_Box, "test")

        wait_and_click_element(self.page, self.PTCMS_Order_textbox)
        self.page.fill(self.PTCMS_Order_textbox, "5")

        # Click Save button
        wait_and_click_element(self.page, self.Add_medical_device_save_button)

        # Click Medical devices availability of activities tab
        wait_and_click_element(self.page, self.Medical_devices_availability_of_activities_tab)

        # Fill out Medical devices availability of activities
        wait_and_click_element(self.page, self.availability_of_activities_Enable_schedule_tasks_Yes_radio_button)

        wait_and_click_element(self.page, self.Activation_Window_start_text_box)
        self.page.fill(self.Activation_Window_start_text_box, "2024-01-01 12:12 AM")

        wait_and_click_element(self.page, self.Activation_Window_end_text_box)
        self.page.fill(self.Activation_Window_end_text_box, "2024-09-12 12:12 AM")

        wait_and_click_element(self.page, self.Start_action_dropdown)
        self.page.fill(self.Start_action_dropdown, "SCREENING")
        self.page.keyboard.press("Enter")

        wait_and_click_element(self.page, self.Start_action_specific_time_point_na_radio_button)
        wait_and_click_element(self.page, self.Start_action_offset_na_radio_button)
        wait_and_click_element(self.page, self.End_action_na_radio_button)
        wait_and_click_element(self.page, self.End_action_specific_time_point_na_radio_button)
        wait_and_click_element(self.page, self.End_action_offset_na_radio_button)
        wait_and_click_element(self.page, self.Window_before_na_radio_button)
        wait_and_click_element(self.page, self.Window_after_na_radio_button)
        wait_and_click_element(self.page, self.Period_na_radio_button)
        wait_and_click_element(self.page, self.Frequency_na_radio_button)
        wait_and_click_element(self.page, self.Max_Frequency_na_radio_button)
        wait_and_click_element(self.page, self.Day_of_week_na_radio_button)
        wait_and_click_element(self.page, self.Time_of_day_na_radio_button)

        # Click Save button
        wait_and_click_element(self.page, self.Add_medical_device_save_button)

        # Click On-demand activity schedule tab
        wait_and_click_element(self.page, self.On_demand_activity_schedule_tab)

        # Fill out On-demand activity schedule tab
        wait_and_click_element(self.page, self.Remote_initiated_na_radio_button)
        wait_and_click_element(self.page, self.Activity_period_na_radio_button)
        wait_and_click_element(self.page, self.Activity_duration_na_radio_button)

        wait_and_click_element(self.page, self.Enable_on_demand_activities_dropdown)
        wait_and_click_element(self.page, self.Enable_on_demand_activities_dropdown_not_availible)

        wait_and_click_element(self.page, self.Track_on_demand_missed_session_dropdown)
        wait_and_click_element(self.page, self.Track_on_demand_missed_session_dropdown_not_availible)

        # Click Save button
        wait_and_click_element(self.page, self.Add_medical_device_save_button)

        # Click Level of Organisation tab
        wait_and_click_element(self.page, self.Level_of_orginisation_tab)

        # Fill out Level of Organisation tab
        wait_and_click_element(self.page, self.Scheduling_Applies_to_level_of_orginisation_dropdown)
        wait_and_click_element(self.page, self.Scheduling_Applies_to_level_of_orginisation_dropdown_study)

        wait_and_click_element(self.page, self.Applicable_countries_for_schedule_all_countries_radio_button)
        wait_and_click_element(self.page, self.Applicable_sites_for_schedule_all_radio_button)

        # Click Save button
        wait_and_click_element(self.page, self.Add_medical_device_save_button)

        # Close Modal
        wait_and_click_element(self.page, self.Add_medical_device_close_button)

    # Fill out Medical Device Content Tab
    def Medical_device_content_tab(self):
        # Click Medical devices content tab
        wait_and_click_element(self.page, self.Medical_devices_content_tab)

        # Settings
        wait_and_click_element(self.page, self.Content_tab_Settings_edit_button)
        wait_and_click_element(self.page, self.Hide_go_to_instruction_button_dropdown)
        wait_and_click_element(self.page, self.Hide_go_to_instruction_button_dropdown_hide)

        # Click Save button
        wait_and_click_element(self.page, self.Add_medical_device_save_button)

        # App content
        wait_and_click_element(self.page, self.App_content_tab)

        wait_and_click_element(self.page, self.UASInstruction_instruction_type_na_radio_button)
        wait_and_click_element(self.page, self.UASInstruction_step_number_na_radio_button)
        wait_and_click_element(self.page, self.UASInstruction_Header_na_radio_button)
        wait_and_click_element(self.page, self.UASInstruction_Body_na_radio_button)
        wait_and_click_element(self.page, self.UASInstruction_Instruction_image_na_radio_button)
        wait_and_click_element(self.page, self.UASInstruction_Video_file_na_radio_button)
        wait_and_click_element(self.page, self.UASInstruction_Video_Cover_Image_na_radio_button)
        wait_and_click_element(self.page, self.UASInstruction_No_Internet_image_na_radio_button)

        wait_and_click_element(self.page, self.UASIntroduction_instruction_type_na_radio_button)
        wait_and_click_element(self.page, self.UASIntroduction_step_number_na_radio_button)
        wait_and_click_element(self.page, self.UASIntroduction_Header_na_radio_button)
        wait_and_click_element(self.page, self.UASIntroduction_Body_na_radio_button)
        wait_and_click_element(self.page, self.UASIntroduction_Instruction_image_na_radio_button)
        wait_and_click_element(self.page, self.UASIntroduction_Video_file_na_radio_button)
        wait_and_click_element(self.page, self.UASIntroduction_Video_Cover_Image_na_radio_button)
        wait_and_click_element(self.page, self.UASIntroduction_No_Internet_image_na_radio_button)

        wait_and_click_element(self.page, self.UASDeviceName_context_type_na_radio_button)
        wait_and_click_element(self.page, self.UASDeviceName_title_intro_na_radio_button)
        wait_and_click_element(self.page, self.UASDeviceName_Description_na_radio_button)
        wait_and_click_element(self.page, self.UASDeviceName_Daisy_chaining_na_radio_button)
        wait_and_click_element(self.page, self.UASDeviceName_Template_na_radio_button)
        wait_and_click_element(self.page, self.UASDeviceName_Identifier_na_radio_button)
        wait_and_click_element(self.page, self.UASDeviceName_title_na_radio_button)
        wait_and_click_element(self.page, self.UASDeviceName_Subheader_na_radio_button)

        # Click Save button
        wait_and_click_element(self.page, self.Add_medical_device_save_button)

        # Web content
        wait_and_click_element(self.page, self.Web_content_tab)

        wait_and_click_element(self.page, self.request_title_text_box)
        self.page.fill(self.request_title_text_box, "test")

        wait_and_click_element(self.page, self.measurment_description_text_area)
        self.page.fill(self.measurment_description_text_area, "test")

        wait_and_click_element(self.page, self.Schedule_description_text_area)
        self.page.fill(self.Schedule_description_text_area, "test")

        wait_and_click_element(self.page, self.Reversibility_spirometry_na_radio_button)
        wait_and_click_element(self.page, self.Description_regarding_na_radio_button)
        wait_and_click_element(self.page, self.Info_in_learn_na_radio_button)

        # Click Save button
        wait_and_click_element(self.page, self.Add_medical_device_save_button)

        # Close Modal
        wait_and_click_element(self.page, self.Add_medical_device_close_button)

        # Click back arrow
        wait_and_click_element(self.page, self.Back_arrow)

