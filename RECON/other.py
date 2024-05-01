import pandas as pd
from datetime import datetime, timedelta

# Generate some sample data for the DataFrame
data = {
    'Services': ['Service A', 'Service B', 'Service C'],
    'Status': ['Success', 'Success', 'Failure'],
    'Comments': ['All good', 'All good', 'Issue found'],
}
df = pd.DataFrame(data)

# Save the DataFrame to an HTML file with colored text
def color_text(val):
    if 'Success' in val:
        return 'color: green'
    elif 'Failure' in val:
        return 'color: red'
    else:
        return ''

styled_df = df.style.applymap(color_text, subset=['Status'])
html = styled_df._render()

# Save the HTML to a file
with open('recon_summary.html', 'w') as file:
    file.write(html)

# Open the HTML file in the default web browser (equivalent to sending the email)
import webbrowser
webbrowser.open('recon_summary.html')
