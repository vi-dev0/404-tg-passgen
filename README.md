<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/vi-dev0/404-tg-passgen">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">TG Password Generator Bot</h3>

  <p align="center">
    A simple password generator Telegram bot
    <br />
    <a href="https://github.com/vi-dev0/404-tg-passgen/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="http://t.me/passgen404_bot">View Demo</a>
    ·
    <a href="https://github.com/vi-dev0/404-tg-passgen/issues">Report Bug</a>
    ·
    <a href="https://github.com/vi-dev0/404-tg-passgen/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#how-it-works">How it works</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://t.me/passgen404_bot)

This is a simple password generator in Telegram.

Bot can generate random passwords (upper/lowercase chars, numbers, special chars), PINs, memorable passwords.

The project was created for the telegram channel - [B4DCAT404](https://t.me/b4dcat404) and to complement the portfolio. The project uses public libraries and generally accepted practices

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With



* [![Telegram][Telegram]][Telegram-url]
* [![Python][Python]][Python-url]
* [![RPG][RPG]][RPG-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

You need 2 packages
* [PyTelegramBotApi](https://pypi.org/project/pyTelegramBotAPI/)
  ```sh
  pip install pyTelegramBotAPI
  ```
* [Random password Generator](https://pypi.org/project/random-password-generator/)
  ```sh
  pip install random-password-generator
  ```

### How it works

For random password generation used library [Random password Generator](https://pypi.org/project/random-password-generator/).
The password is generated using uppercase, lowercase letters, numbers and special characters.

For PINs generation used *random* module from Python.

For Memorable passwords used [dictionary](#)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To generate random password tap **Random password**

To generate PINs tap **PIN**, chose number of digits and tap on it.

To generate memorable password tap **Memorable password**

All passwords can be copied, just click on any password or PIN and they will be copied

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [x] Create bot by [BotFather](https://t.me/BotFather)
- [x] Found library for password generation
- [x] Add types of passwords
    - [] Random password
    - [x] PINs
    - [x] Memorable password
- [x] Commit and push on GitHub
- [x] Publish in [B4DCAT404](https://t.me/b4dcat404) chanel

See the [open issues](https://github.com/vi-dev0/404-tg-passgen/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Vi - [@vi_dev0](https://twitter.com/vi_dev0)

Project Link: [https://github.com/vi-dev0/404-tg-passgen](https://github.com/vi-dev0/404-tg-passgen)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

I used these resources while creating the bot

* [Telegram Bot API official](https://core.telegram.org/bots/api#inlinekeyboardmarkup)
* [Telegram Bot API (repo)](https://github.com/eternnoir/pyTelegramBotAPI)
* [Random password generator package](https://pypi.org/project/random-password-generator/)
* [Open Source License](https://choosealicense.com)
* [Img Shields](https://shields.io)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/vi-dev0/404-tg-passgen.svg?style=for-the-badge
[contributors-url]: https://github.com/vi-dev0/404-tg-passgen/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/vi-dev0/404-tg-passgen.svg?style=for-the-badge
[forks-url]: https://github.com/vi-dev0/404-tg-passgen/network/members
[stars-shield]: https://img.shields.io/github/stars/vi-dev0/404-tg-passgen.svg?style=for-the-badge
[stars-url]: https://github.com/vi-dev0/404-tg-passgen/stargazers
[issues-shield]: https://img.shields.io/github/issues/vi-dev0/404-tg-passgen.svg?style=for-the-badge
[issues-url]: https://github.com/vi-dev0/404-tg-passgen/issues
[license-shield]: https://img.shields.io/github/license/vi-dev0/404-tg-passgen.svg?style=for-the-badge
[license-url]: https://github.com/vi-dev0/404-tg-passgen/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/b4dcat404
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Telegram]: https://img.shields.io/badge/telegram-blue?style=for-the-badge&logo=telegram&logoColor=white
[Telegram-url]: https://telegmra.org/
[Python]: https://img.shields.io/badge/python-blue?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://pythong.org
[RPG]: https://img.shields.io/badge/RPG-blue?style=for-the-badge&logo=python&logoColor=white
[RPG-url]: https://pypi.org/project/random-password-generator/