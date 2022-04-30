const fakeNews = ['A cat scored a goal at the World Cup.','Hurricane Harvey hit Texas in August, evacuating thousands. A Canadian imam has been accused of denying Christian victims refuge in a mosque.','The U.S. found that each mask contained an antenna that China used to steal the privacy of the American people.','There is news that the millimeter-wave spectrum used by 5G technology may spread the new coronavirus.','Alien invasion of Earth','A softball pitcher named Sid Finch, who can throw a ball at 150 miles an hour','Six-year-old boy mistakenly carried 2,000 meters in a helium balloon','Bananas and rock sugar can cure a cough','Gargling warm water with salt or vinegar can cure Covid-19','Everyone can get rich through the Internet','Musk has successfully landed on Mars!','Lebron James won the playoffs this year']
const realNews = ['13-year-old boy made $300 by reselling sneakers.','The 105-year-old posted a selfie on social media.','Barcelona 1-1 draw with Real Madrid.','Due to the impact of the epidemic, many countries have blocked coastal ports and borders.','The U.S. found that each mask contained an antenna that China used to steal the privacy of the American people.','Roger Federer is the tennis world champion!','The Covid-19 may cause irreversible damage to human physiological functions','The Australian border reopened this year']
function Food(gameSnake) {
    var self = this;

    do {
        // 食物的位置
        this.row = parseInt(Math.random() * gameSnake.row)
        this.col = parseInt(Math.random() * gameSnake.col)
        this.isfake = Math.random() >= 0.5;
        if(this.isfake){
            this.news = fakeNews[Math.floor(Math.random()*fakeNews.length)]
        }else{
            this.news = realNews[Math.floor(Math.random()*realNews.length)]
        }

    } while ((function () {
        // 遍历蛇的 row col 然后和 food 新随机出来的 row col 进行判断，是否重合
        for (var i = 0; i < gameSnake.snake.body.length; i++) {
            if (self.row == gameSnake.snake.body[i].row && self.col == gameSnake.snake.body[i].col) {

                return true;
            }
        }
        return false;
    })());
}
Food.prototype.render = function () {
    game.setHTML(this.row, this.col);
    document.getElementById('dCenter').innerHTML = this.news;
}