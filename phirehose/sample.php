<?PHP
require_once("hose/lib/Phirehose.php");

class SampleConsumer extends Phirehose {

	public function enqueueStatus($status) {
		/*
		$data = json_decode($status, true);
		if(is_array($data) && isset($data['user']['screen_name'])) {
			print $data['user']['screen_name'].': '.urldecode($data['text'])."<br />";
		}
		*/
		$decode = json_decode($status, true);
		if($decode['user']['lang'] == 'en'){
			$user = $decode['user']['screen_name'];
			$post = $decode['text'];

			echo $user.": ".$post."<br />";
		}


		/*	
		echo "<pre>";
		print_r($decode);	
		echo "</pre>";
		*/
	}
}

$sc = new SampleConsumer('zandermane', 'alex18257', Phirehose::METHOD_SAMPLE);
$sc->consume();
