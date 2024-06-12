from uvicorn import run

if __name__ == "__main__":
    run(app="game.main.server.server:app", host="127.0.0.1", port=5000, reload=True)
