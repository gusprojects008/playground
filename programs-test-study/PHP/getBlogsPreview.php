<?php

/*$blogsDir = __DIR__ . '../blogs/contents'*/
/*$homeDir = getenv('HOME');*/
$blogsDir = '../blogs/contents';
$blogs = [];

if (is_dir($blogsDir)) {
    $files = scandir($blogsDir);
    foreach ($files as $file) {
      if (pathinfo($file, PATHINFO_EXTENSION) === 'html') {
        $filePath = $blogsDir . '/' . $file;
        $content = file_get_contents($filePath);

        preg_match('/<title>(.*?)<\\/title>/i', $content, $titleMatches);
        $title = $titleMatches[1] ?? 'Untitled Blog';
        

        preg_match('/<img[^>]+src="([^">]+)"/i', $content, $imageMatches);
        $image = $imageMatches[1] ?? null;

        $blogs[] = [
          'title' => $title,
          'filename' => $file,
          'image' => $image ? : null
        ]; 
      };
    };
};

header('Content-Type: application/json');
echo json_encode($blogs);

