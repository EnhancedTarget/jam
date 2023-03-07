# Cisco Jam 2023

## Round 3

This round will incorporate some real-world examples of Software Dev into the challenges, by using various [APIs](https://medium.com/@perrysetgo/what-exactly-is-an-api-69f36968a41f).
In simple terms, an API just allows different applications to talk to each other. You will encounter APIs in many places in your career, and as you progress through your degree.

---

### Challenge 3.1: Weather API

In these challenges, the aim is to configure your bot to be able to accept weather related queries, send a request to [Open-Meteo](https://open-meteo.com/en/docs/) to retrieve weather info, and return the right results.

Firstly, when the bot receives the "weather" command (with nothing else), have the bot return the highest temperature recorded in Galway yesterday.

```
You:
> @YourBot weather

Bot:
> Yesterday, in Galway, the highest temperature recorded was 20 degrees celsius.
```

### Challenge 3.2

When the bot receives an input after the "weather" command, you can assume that this is a city. For simplicity, allowed cities are: Galway, Oslo, London.

Return the highest temperature recorded for the given city.

```
You:
> @YourBot weather Oslo

Bot:
> Yesterday, in Oslo, the highest temperature recorded was 17 degrees celsius.
```

### Challenge 3.3

If your bot receives an input after the city, you can assume that the type of measurement is given. For simplicity, allowed measurements are: temperature, rain, wind.

Given a city **and a measurement type**, return the correct maximum reading for yesterday.

```
You:
> @YourBot weather London rain

Bot:
> Yesterday, in London, the total rainfall recorded was 10mm.
```

```
You:
> @YourBot weather Galway wind

Bot:
> Yesterday, in Galway, the highest windspeed recorded was 5km/h.
```

**Bonus points:** If an invalid city or measurement is specified (ie, not any of the ones mentioned above), return any kind of helpful error message. Eg: "Invalid input. Expected format: **weather (city) (measurement)**".
