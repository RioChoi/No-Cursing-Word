<script>

    import {afterUpdate} from 'svelte'

    export let word;

    afterUpdate(async (promise) => {
        console.log(word)
        let box = document.querySelector("#kk");
        box.innerHTML = "<div id=\"ff\"></div>"

        console.log("생성됨")

        for (var i = 0; i < word.length; i++) {
            const dd = document.createElement('div');
            var word_meaning = word[i][3]
            var word_usage = word[i][4]

            if (word_meaning == "") {
                word_meaning = "사전에 설명이 없습니다 🥹"
            }
            if (word_usage == "") {
                word_usage = "사전에 용례가 없습니다 🥹"
            }
            dd.innerHTML = 
            "<br>" +
            "<h4>" +
                "<mark>" + word[i][2] + "</mark>" +
            "</h4>" +
            "<div style=\"text-align:right\"><i style=\"color:Gray\">#" + word[i][1] + "</i></div>" +
            "<div id=\"textbox\">" +
                "<div>뜻 :</div>" +
                "<p>" + word_meaning + "</p>" +
                "<div>용례 :</div>" +
                "<p>" + word_usage + "</p>"
            "</div>"
            
            document.querySelector('#ff').appendChild(dd);
            console.log(word[i][2]);
        }
    });

</script>