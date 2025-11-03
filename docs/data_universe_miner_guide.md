# Data Universe Miner Guide

This guide provides a comprehensive overview of how to set up, configure, and run a miner for the Bittensor Subnet 13, also known as the Data Universe.

## 1. Introduction

The Data Universe is a Bittensor subnet dedicated to building a decentralized data layer. Miners are rewarded for scraping data from various sources and making it available to the network.

This guide will walk you through the entire process of becoming a successful miner on Subnet 13, from setting up your environment to keeping your miner running and profitable.

## 2. Prerequisites

Before you begin, ensure you have the following prerequisites:

### Hardware

- A machine with sufficient network bandwidth and disk space. A GPU is not required.

### Software

- Python 3.10 or higher.
- `git` for cloning the repository.
- `pm2` for managing the miner process.

### Accounts

- A Bittensor wallet with a registered hotkey.
- An Apify account and API token (for scraping Twitter).
- A YouTube API key, OAuth Client ID, and Client Secret (for scraping YouTube).

## 3. Setup and Configuration

### 3.1. Clone the Repository

Clone the `data-universe` repository from GitHub:

```shell
git clone https://github.com/macrocosm-os/data-universe.git
cd data-universe
```

### 3.2. Create a Virtual Environment

Create and activate a Python virtual environment:

```shell
python3 -m venv venv
source venv/bin/activate
```

### 3.3. Install Dependencies

Install the required Python packages:

```shell
pip install -e .
```

### 3.4. Create the `.env` File

Create a `.env` file in the root of the `data-universe` directory and add your API keys and tokens:

```
APIFY_API_TOKEN=your_apify_api_token
YOUTUBE_API_KEY=your_youtube_api_key
YOUTUBE_OAUTH_CLIENT_ID=your_youtube_oauth_client_id
YOUTUBE_OAUTH_CLIENT_SECRET=your_youtube_oauth_client_secret
```

### 3.5. Configure the `scraping_config.json` File

The `scraping_config.json` file determines what data your miner will scrape. You need to configure it to scrape the incentivized tags from the `gravity` repository.

**[This section will be updated with the script to automatically fetch and update the incentivized tags.]**

## 4. Deployment and Monitoring

### 4.1. Running the Miner

Use `pm2` to run the miner as a background process:

```shell
pm2 start venv/bin/python -- ./neurons/miner.py --wallet.name your_wallet_name --wallet.hotkey your_hotkey_name
```

### 4.2. Monitoring the Miner

You can monitor the miner using the following `pm2` commands:

- **Check the status of the miner:**
  ```shell
  pm2 status
  ```
- **View the logs:**
  ```shell
  pm2 logs 0
  ```
- **Monitor the miner in real-time:**
  ```shell
  pm2 monit
  ```

## 5. Dynamic Desirability

The list of incentivized tags is dynamic and changes over time. To remain profitable, you need to keep your `scraping_config.json` file up-to-date.

**[This section will be updated with the script to automatically check for updates and reconfigure the miner.]**

## 6. Troubleshooting

**[This section will be updated with common errors and their solutions.]**

## 7. Websites

Here is a list of relevant websites with a brief explanation of each:

- **Macrocosmos Documentation:**
  - `https://docs.macrocosmos.ai/subnets/subnet-13-data-universe`: The official documentation for Subnet 13.
  - `https://docs.macrocosmos.ai/about-us/subnet-status-update`: Subnet status updates from the Macrocosmos team.
  - `https://docs.macrocosm.ai/about-us/news-and-updates`: News and updates from the Macrocosmos team.
- **GitHub Repositories:**
  - `https://github.com/macrocosm-os/data-universe`: The main repository for the Data Universe subnet.
  - `https://github.com/macrocosm-os/gravity`: The repository containing the dynamic desirability data.
  - `https://github.com/macrocosm-os/data-universe-api`: The API for the Data Universe.
- **Social Media:**
  - `https://x.com/MacrocosmosAI`: The official X.com account for Macrocosmos.
  - `https://discord.gg/bittensor`: The official Bittensor Discord server.
- **Tools:**
  - `https://docs.macrocosmos.ai/constellation-user-guides/nebula`: The user guide for the Nebula data visualizer.
  - `https://docs.macrocosmos.ai/developers/tools/macrocosmos-mcp`: The documentation for the Macrocosmos Model Context Protocol.
  - `https://wandb.ai/macrocosmos/data-universe-validators`: The Weights & Biases dashboard for the validators.
  - `https://pm2.keymetrics.io/docs/usage/quick-start/`: The official documentation for `pm2`.