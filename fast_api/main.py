import uvicorn


uvicorn.run(app="app:app", log_level='debug',
            host='0.0.0.0', port=8999, workers=1)
