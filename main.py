import flask
import dash
import os
import apps.py.export
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from flask import send_from_directory
import pandas as pd
import requests
## Weather Arse
arse_lelijk = {
                "number": '7464963',
                "body": "open_weather_api",
                "temp": [
                {
                "est": "19",
                "min": "14"
                    }, 
                    {
                "est": "19",
                "min": "13"
                    }, 
                    {
                "est": "18",
                "min": "12"
                    }
                ]
        }

# Data of cities from here:
# https://github.com/spatie/belgian-cities-geocoded/blob/master/belgian-cities-geocoded.csv

def ExtractCities():
    citylist = pd.read_csv('../data/belgian-cities-geocoded.csv').to_list('name').str().strip().lower()
    counter = 0
    for obj in citylist:
        print(counter)
        counter = counter + 1
        weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' +str(obj) + '&units=metric&lang=en&appid=c0c4a4b4047b97ebc5948ac9c48c0559' 
        try :
            response = requests.get(weather_url)
        except:
            break
        weather = response['body']['temp'][0:2]
        print(weather)
        if weather == arse_lelijk:
            print('!!!!!!!!!!!!!!!!!!')
            print('found at city id:', counter)
        else:
            continue

# Create/transfer Dash variable 
city = export(city)

###### -------------------
# DASH SECTION
###### -------------------

app = dash.Dash()

app.layout = html.Div(
    <?php
        $city    = &VAR.py(city);
            $jsonfile    = file_get_contents( 'http://api.openweathermap.org/data/2.5/weather?q=' . $city . '&units=metric&lang=en&appid=c0c4a4b4047b97ebc5948ac9c48c0559' );
            $jsondata    = json_decode( $jsonfile );
            $temp        = $jsondata->main->temp;
            $pressure    = $jsondata->main->pressure;
            $mintemp     = $jsondata->main->temp_min;
            $maxtemp     = $jsondata->main->temp_max;
            $wind        = $jsondata->wind->speed;
            $humidity    = $jsondata->main->humidity;
            $desc        = $jsondata->weather[0]->description;
            $maind       = $jsondata->weather[0]->main;
            $currentTime = time();
            ?>
            <style>
            body {
                font-family: Arial;
                font-size: 0.95em;
                color: #929292;
            
            }
            
            .report-container {
                border: #E0E0E0 1px solid;
                padding: 20px 40px 40px 40px;
                border-radius: 2px;
                width: 550px;
                margin: 0 auto;
            }
            
            .weather-icon {
                vertical-align: middle;
                margin-right: 20px;
            }
            
            .weather-forecast {
                color: #212121;
                font-size: 1.2em;
                font-weight: bold;
                margin: 20px 0px;
            }
            
            span.min-temperature {
                margin-left: 15px;
                color: #929292;
            }
            
            .time {
                line-height: 25px;
            }
            </style>
            <body>
            <div class="report-container">
                    <h2><?php echo $jsondata->name; ?> Weather Status</h2>
                    <div class="time">
                        <div><?php echo date( 'l g:i a', $currentTime ); ?></div>
                        <div><?php echo date( 'jS F, Y', $currentTime ); ?></div>
                        <div><?php echo $desc; ?></div>
                    </div>
                    <div class="weather-forecast">
                        <img
                            src="http://openweathermap.org/img/w/<?php echo $jsondata->weather[0]->icon; ?>.png"
                            class="weather-icon" /> <?php echo $mintemp; ?>°C<span
                            class="min-temperature"><?php echo $maxtemp; ?>°C</span>
                    </div>
                    <div class="time">
                        <div>Humidity: <?php echo $humidity; ?> %</div>
                        <div>Wind: <?php echo $wind; ?> km/h</div>
                    </div>
                </div>
                </body>


if __name__ == '__main__':
    app.run_server(debug=True)
