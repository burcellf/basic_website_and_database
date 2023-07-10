from website import create_app # import the function from '__init__.py'

app = create_app()

# prevent app.run() from being called if
# 'main.py' is imported into another project
if __name__ == '__main__':
    
    # debug automatically refreshes the server
    # whenever there's a change to the code
    app.run(debug=True)

