from selenium.webdriver.chrome.options import Options
options = ChromeOptions()
options.browser_version = "107.0"
options.platform_name = "Windows 10"
lt_options = {};
lt_options["username"] = "eezipc";
lt_options["accessKey"] = "AqaF77qf1hc1y2bzbXcD3PZl32nhsVAV7ZTxPCVczoGfdFI9R8";
lt_options["geoLocation"] = "GR";
lt_options["visual"] = True;
lt_options["timezone"] = "UTC+03:00";
lt_options["build"] = "buildname";
lt_options["project"] = "projectname";
lt_options["name"] = "testname";
lt_options["console"] = "false";
lt_options["networkThrottling"] = "Regular 4G";
lt_options["selenium_version"] = "4.0.0";
lt_options["w3c"] = True;
options.set_capability('LT:Options', lt_options);