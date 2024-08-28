<?php
class AdminPage{
    public function __construct(){
    }

    public function handleRequest(){
        if ($_SERVER['HTTP_HOST'] === 'real_secure_host') {
            echo "There's nothing here, for real....";
            if (isset($_REQUEST['object'])) {
                $serializedData = $_REQUEST['object'];
                $var1 = $this->safeUnserialize($serializedData);
                if ($var1 instanceof ObjectCompiler) {
                    $var1->execute();
                }
            } else {
                echo "Told you it won't work.";
            }
        } else {
            header("HTTP/1.0 403 Forbidden");
            echo "This one is still under construction, take a look at the other page please.";
        }
    }

    private function safeUnserialize($data){
        $unserializedData = unserialize($data);
        if ($unserializedData === false) {
            throw new Exception("What happenned????");
        }

        return $unserializedData;
    }
}

class ObjectCompiler{
    public $objection;

    public function __construct(){
    }

    public function execute(){
        if (isset($this->objection)) {
            eval($this->objection);
        }
    }
}

$adminPage = new AdminPage();
$adminPage->handleRequest();
?>