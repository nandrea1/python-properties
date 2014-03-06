<b>This library allows you to read .properties files in python. Properties files are a simple way to enable program configuration that does not require a code change. These properties files should be formatted as such: "property=value", with each property on a new line. Library methods are as follows:</b>

<b>Properties</b>(filepath):
  Constructor to create the properties object. Requires that you pass in the filepath of the properties file
  
<b>getProperty</b>(property name):
  Similar to getProperty java command. Requires the name of the property and returns the value associated with that      property
  
  <b>setProperty</b>(property name, value):
Allows the user to set the value of a specific property. Note that this only changes the local value of that property, and does not write the new value to the file
    
