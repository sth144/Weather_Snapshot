/***************************************************************************************************
  Title: JavaScript CSV Export
  Author: Sean Hinds
  Date: 03/13/18
  Description: CSV export function. Parses a table for data and generates a text string from that
                data. Formats that text data for .csv. Generates a temporary link element which
                initiates .csv download to the client.
***************************************************************************************************/

function csvExport() {

  console.log('export');

  var text = "";

  /* Target table */
  var tab = document.getElementById('tab');

  // Iterate through rows in the table
  for (var j = 0; j < tab.rows.length; j++) {

    var row = tab.rows[j];
    var children = row.getElementsByTagName('td') || row.getElementsByTagName('th');

    if (row.style.display != 'none') {
      // Iterate through each data elemet in the row
      for (var i = 0; i < children.length; i++) {

        // Add inner HTML of element to text variable
        text += children[i].innerHTML + ',';

      }

      // Next row
      text += "\n";
    }

  }

  // Create a temporary element
  var element = document.createElement('a');

  // Set the element to download a .csv file encoded using text
  element.setAttribute('href', 'data:text/csv;charset=UTF-8,' + encodeURIComponent(text));
  element.setAttribute('download', 'export.csv');

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);

}
