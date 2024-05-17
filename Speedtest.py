import speedtest

def test_speed():
    st = speedtest.Speedtest()
    st.download()  # Perform download test
    st.upload()  # Perform upload test
    st.results.share()  # Share the result

    results_dict = st.results.dict()

    print(f"Download speed: {results_dict['download'] / 1_000_000:.2f} Mbps")
    print(f"Upload speed: {results_dict['upload'] / 1_000_000:.2f} Mbps")
    print(f"Ping: {results_dict['ping']} ms")
    print(f"Server: {results_dict['server']['name']} located in {results_dict['server']['country']}")

if __name__ == "__main__":
    test_speed()
