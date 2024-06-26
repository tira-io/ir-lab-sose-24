build-ui-docker:
	./ir-components-archive/create_ir_components_archive.py
	docker run --rm -v ${PWD}:/app -v ${PWD}/static/dist/:/dist -w /app/ui --entrypoint vite mam10eks/github-page-tutorial:0.0.2 build

coverage:
	 pytest --cov=construct_indices \
	 && coverage-badge -o construct_indices/coverage.svg
