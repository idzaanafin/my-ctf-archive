<?php

if (!isset($_GET['url'])) {
    die("You might forgetting something. What about the 'url' param?");
}

$target_url = $_GET['url'];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $target_url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
$response = curl_exec($ch);

if ($response === false) {
    die("Some unknown force have stopped the service!");
}

curl_close($ch);
echo "Well that's it :v";
?>