# CryptoWorld - Crypto Currency & Blockchain News

CryptoWorld is a modern Django-based web application that provides real-time cryptocurrency prices and the latest blockchain news. It leverages the CryptoCompare API to fetch up-to-date information for major cryptocurrencies like Bitcoin, Ethereum, and more.

## Features

- **Real-time Price Tracking:** View current prices, daily highs, daily lows, and market capitalization for top cryptocurrencies.
- **Latest Crypto News:** Stay informed with a curated feed of the latest news from the blockchain and crypto industry.
- **Responsive Design:** A clean and modern user interface built with Bootstrap 5, ensuring a great experience on both desktop and mobile devices.
- **Clean Codebase:** Updated to Django 4.2 with modern Python practices and streamlined dependencies.

## Technologies Used

- **Backend:** Django 4.2 (Python 3)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Data Source:** [CryptoCompare API](https://min-api.cryptocompare.com/)
- **HTTP Client:** Requests

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd cryptonews
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

5. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:8000/`

## Project Structure

- `crypto/`: The main application directory containing views, templates, and URLs.
- `cryptonews/`: The project configuration directory.
- `requirements.txt`: List of Python dependencies.
- `manage.py`: Django management script.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
