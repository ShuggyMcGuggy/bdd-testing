Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!
      
  Scenario: Check the spreadsheet Format
      Given We load a specified spreadsheet
        When We check the column headings
        Then We will report an error with enough test to ideintify the problem
      
      
    