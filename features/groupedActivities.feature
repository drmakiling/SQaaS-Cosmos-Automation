Feature: Grouped Activities

    @19337
    @groupedActivities
    Scenario: Given On_{Win}_{Chrome} and On_Cosmos_Site and Signed_in_{StudyBA}_user and Draft_Study_{MyStudies} and Config_Alert_Off When Click_Grouped_activities_feature Then Verify_Grouped_activities_feature_page
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Grouped activities" feature nav menu option
        And config alert is "off"
        Then Grouped Activities feature page is empty

    @19364
    @groupedActivities
    Scenario: Given On_{Win}_{Chrome} and On_Cosmos_Site and Signed_in_{StudyBA}_user and Draft_Study_{MyStudies} and [Not] Config_Alert_Off When Click_Grouped_activities_feature Then Verify_Grouped_activities_feature_page
        Given the user is logged in as "STUDYBA1"
        And create or select a case a study
        And click "Grouped activities" feature nav menu option
        And config alert is "on"
        Then Grouped Activities feature page is empty