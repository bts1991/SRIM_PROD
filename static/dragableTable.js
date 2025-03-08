
// 드래그 앤 드롭을 위한 이벤트 리스너 등록
document.addEventListener('DOMContentLoaded', () => {

    // tbody 요소의 모든 자식 요소 중 tr 요소를 선택하여 rows 변수에 할당
    const rows = document.querySelectorAll('tbody > tr');
    // rows에 forEach 메서드를 호출하여 각각의 tr 요소에 대해 드래그 이벤트 리스너를 등록
    rows.forEach(row => {
    // 드래그가 가능하도록 draggable속성을 true로 설정
    row.draggable = true;
    // 드래그 이벤트가 시작될 때 실행할 콜백 함수 등록
    row.addEventListener('dragstart', e => {
    
    //drag와 관련된 이벤트에서는 모두 DataTransfer 객체를 사용할 수 있다.
    //dataTransfer 객체가 setData()함수를 제공.
    //setData():데이터를 드래그할 때 전달하고자 하는 정보를 설정하는 메서드. 
    //첫 번째 인자로 데이터의 형식을 지정할 수 있으며, 두 번째 인자로 전달하려는 값(value)을 지정.
    // setData 메서드를 호출하여 드래그 데이터 설정 - 데이터 형식은 text/plain, 값은 해당 tr 요소의 id 값.
    //이렇게 설정된 드래그 데이터는 드래그 이벤트가 발생할 때 dataTransfer 객체에 저장되어 드롭 이벤트가 발생할 때 사용된다.
    e.dataTransfer.setData('text/plain', row.id);

	});
});
});

// tbody 요소에 드롭 이벤트 리스너 등록
const dropzone = document.querySelector('tbody');

dropzone.addEventListener('dragover', e => {

    // 기본 이벤트 동작을 막음
    e.preventDefault();
    
    // 드래그된 요소를 드롭할 위치를 계산하는 함수를 호출하여 그 결과값을 afterElement 변수에 할당
    const afterElement = getDragAfterElement(dropzone, e.clientY);
    
    // dragging 클래스를 가진 요소를 선택하여 draggable 변수에 할당
    const draggable = document.querySelector('.dragging');
    
    // afterElement가 null일 경우, 마지막 자식 요소로 추가하고 그렇지 않은 경우, afterElement 바로 전 위치에 추가
    if (afterElement == null) {
    	dropzone.appendChild(draggable);
    } else {
    	dropzone.insertBefore(draggable, afterElement);
    }
});

// 드롭 대상 행 중 이동할 위치를 결정하는 함수
function getDragAfterElement(container, y) {

    // container 내의 모든 tr 요소들 중 dragging 클래스를 가지지 않은 요소들을 선택하여 draggableElements 변수에 할당
    const draggableElements = [...container.querySelectorAll('tr:not(.dragging)')];
    
    // draggableElements 배열을 reduce 메서드를 이용하여 y값에 따라 가장 근접한 요소를 찾아낸다.
    return draggableElements.reduce((closest, child) => {

	const box = child.getBoundingClientRect();
    
	// 드래그 위치 - 드롭 대상 요소의 top 위치 - 드롭 대상 요소의 높이 / 2 값을 offset 변수에 할당
	const offset = y - box.top - box.height / 2;
    
	// offset 값이 음수이고 closest.offset보다 더 큰 경우, closest를 현재 child 요소로 대체
        if (offset < 0 && offset > closest.offset) {
            return { offset: offset, element: child };
        } else {
            return closest;
        }
	}, { offset: Number.NEGATIVE_INFINITY }).element;
    // reduce 함수에서 초기 값으로 사용되는 객체. 
    //offset 속성은 "-Infinity"로 설정하여, reduce 함수가 실행되면서 만들어지는 첫 closest.offset 값이 항상 offset보다 크도록 보장한다.
}

// 드래그 중인 행의 스타일 설정.
//'dragging' 클래스는 드래그 중인 요소를 스타일링하기 위해 사용되므로 드래그가 종료되면 스타일링 제거
// 어떤 요소에서든지 드래그 이벤트가 발생하면 실행됨
document.addEventListener('dragend', e => {

    // 'dragend' 이벤트가 발생한 요소 중 가장 가까운 <tr> 요소를 찾아서
    const draggable = e.target.closest('tr');
    // 해당 <tr> 요소의 'dragging' 클래스를 제거하기
    draggable.classList.remove('dragging');
})
;