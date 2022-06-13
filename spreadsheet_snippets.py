def create(service):
    spreadsheet = {
        'properties': {
            'title': 'example title use gsheet api'
        }
    }
    spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                                fields='spreadsheetId').execute()
    print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))
    return spreadsheet


def append(service, list_value, spreadsheet_id):
    values = [
        list_value,
        # Additional rows ...
    ]
    body = {
        'values': values
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range='sheet1',
        valueInputOption='USER_ENTERED', body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))


def get(service, spreadsheet_id, ):
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range='sheet1!2:2').execute()
    rows = result.get('values', [])
    print(rows)