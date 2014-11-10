<?php
  $url = 'https://api.jcdecaux.com/vls/v1/stations/10025?contract=paris&apiKey=XXX';
  $json = file_get_contents($url);
  $data = json_decode($json,true);
  $nb1 = $data['available_bikes'];
  echo $nb1;
?>
